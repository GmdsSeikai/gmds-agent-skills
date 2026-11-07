"""Exercise the annotation CLI using synthetic pixels and bundled fonts."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import fitz


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "annotate_visual.py"


class AnnotateVisualTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(prefix="annotate-visual-test-")
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.source = self.root / "原图.png"
        with fitz.open() as document:
            page = document.new_page(width=240, height=120)
            page.draw_rect(fitz.Rect(40, 40, 60, 60), color=None, fill=(1, 0, 0))
            page.draw_rect(fitz.Rect(170, 80, 190, 100), color=None, fill=(0, 0, 1))
            self.source.write_bytes(page.get_pixmap(alpha=False).tobytes("png"))
        self.spec_path = self.root / "标注.json"
        self.out = self.root / "output"
        self.spec = {"version": 1, "title": "教学标注 · 合成图", "callouts": [
            {"text": "1 红色节点", "target": [50, 50], "label": [-170, 20]},
            {"text": "2 蓝色节点", "target": [180, 90], "label": [250, 70], "via": [[245, 90]]},
        ]}

    def run_cli(self, *options, source=None, spec=None, out=None):
        self.spec_path.write_text(json.dumps(self.spec if spec is None else spec, ensure_ascii=False), encoding="utf-8")
        return subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(SCRIPT), str(source or self.source),
             str(self.spec_path), "--out", str(out or self.out), *options],
            capture_output=True, text=True, encoding="utf-8", timeout=30,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_original_bytes_and_pixel_coordinates_preserved(self):
        before = hashlib.sha256(self.source.read_bytes()).digest()
        result = self.run_cli()
        self.assert_success(result)
        clean = next(self.out.glob("*.original.png"))
        annotated = next(self.out.glob("*.annotated.png"))
        self.assertEqual(clean.read_bytes(), self.source.read_bytes())
        self.assertEqual(hashlib.sha256(self.source.read_bytes()).digest(), before)
        self.assertIn(str(clean.resolve()), result.stdout)
        self.assertIn(str(annotated.resolve()), result.stdout)
        image = fitz.Pixmap(str(annotated))
        self.assertEqual((image.width, image.height), (640, 520))
        # Source is offset by 200, not scaled; inspect away from leader endpoints.
        self.assertEqual(image.pixel(245, 245)[:3], (255, 0, 0))
        self.assertEqual(image.pixel(385, 295)[:3], (0, 0, 255))
        self.assertEqual(image.pixel(300, 260)[:3], (255, 255, 255))
        # The leader's target has the known source-to-canvas offset.
        self.assertNotEqual(image.pixel(249, 250)[:3], (255, 0, 0))

    def test_cjk_text_is_visible_in_margin_without_covering_source(self):
        self.assert_success(self.run_cli())
        image = fitz.Pixmap(str(next(self.out.glob("*.annotated.png"))))
        # Expected CJK text region, clear of the label's right-edge leader.
        ink = sum(image.pixel(x, y)[:3] != (255, 255, 255)
                  for x in range(44, 125) for y in range(220, 244))
        self.assertGreater(ink, 200)
        # An untouched source strip retains every pixel after composition.
        original = fitz.Pixmap(str(self.source))
        for x in range(80, 160):
            for y in range(40, 80):
                self.assertEqual(image.pixel(x + 200, y + 200), original.pixel(x, y))

    def test_existing_names_and_same_basename_are_never_overwritten(self):
        self.out.mkdir()
        sentinel = self.out / "原图.original.png"
        sentinel.write_bytes(b"preserve existing")
        self.assert_success(self.run_cli())
        prior = {path: path.read_bytes() for path in self.out.iterdir()}
        sibling = self.root / "sibling"
        sibling.mkdir()
        alternate = sibling / self.source.name
        alternate.write_bytes(self.source.read_bytes())
        self.assert_success(self.run_cli(source=alternate))
        for path, contents in prior.items():
            self.assertEqual(path.read_bytes(), contents)
        self.assertEqual(len(list(self.out.glob("*.png"))), 5)
        self.assertEqual(sentinel.read_bytes(), b"preserve existing")

    def test_invalid_spec_rejected_before_output(self):
        cases = [
            {**self.spec, "version": 2}, {**self.spec, "version": True},
            {**self.spec, "extra": "unknown"}, {**self.spec, "callouts": []},
            {**self.spec, "title": ""}, {**self.spec, "title": "line\nbreak"},
        ]
        for replacement in (
            {"target": [-1, 50]}, {"target": [240, 50]}, {"target": [50, float("nan")]},
            {"target": [True, 50]}, {"target": [50]}, {"label": [0, 0]},
            {"label": [-201, 0]}, {"label": [420, 0]}, {"text": ""},
            {"via": [[999, 0]]}, {"via": "wrong"}, {"extra": 1},
        ):
            cases.append({**self.spec, "callouts": [{**self.spec["callouts"][0], **replacement}]})
        cases.append({**self.spec, "callouts": [self.spec["callouts"][0]] * 2})
        for spec in cases:
            with self.subTest(spec=spec):
                result = self.run_cli(spec=spec)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("no output created", result.stderr)
                self.assertNotIn("Traceback", result.stderr)
                self.assertFalse(self.out.exists())

    def test_font_missing_glyphs_fail_instead_of_blank_success(self):
        font_file = self.root / "latin-only.ttf"
        font_file.write_bytes(fitz.Font("helv").buffer)
        result = self.run_cli("--font", str(font_file))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("font lacks glyphs", result.stderr)
        self.assertFalse(self.out.exists())
        result = self.run_cli("--font", str(self.root / "missing.ttf"))
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.out.exists())

    def test_invalid_source_and_cli_leave_no_output(self):
        bad = self.root / "bad.png"
        bad.write_bytes(b"not a png")
        for source in (self.root / "missing.png", bad):
            with self.subTest(source=source):
                result = self.run_cli(source=source)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.out.exists())
        for option in (("--padding", "0"), ("--font-size", "-1")):
            result = self.run_cli(*option)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(self.out.exists())

    def test_output_failure_is_clear_and_preserves_existing_file(self):
        blocked = self.root / "blocked"
        blocked.write_bytes(b"keep")
        result = self.run_cli(out=blocked / "child")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("earlier exports are retained", result.stderr)
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(blocked.read_bytes(), b"keep")


if __name__ == "__main__":
    unittest.main()
