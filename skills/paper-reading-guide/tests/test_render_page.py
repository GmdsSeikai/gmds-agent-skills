"""Exercise the real CLI with generated PDFs; no paper fixtures or extra packages."""
import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import fitz


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "render_page.py"


class RenderPageTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory(prefix="render-page-test-")
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        self.pdf = self.root / "合成 fixture.pdf"
        self.out = self.root / "output"
        self.make_pdf(self.pdf)

    @staticmethod
    def make_pdf(path, rotation=0, cropped=False, pages=1, red=(1, 0, 0)):
        """Place known colors using source coordinates, before any page rotation."""
        box = (40, 60, 560, 740) if cropped else (0, 0, 600, 800)
        x0, y0, x1, y1 = box
        with fitz.open() as document:
            for _ in range(pages):
                page = document.new_page(width=600, height=800)
                marks = (
                    (x0 + 30, y0 + 30, red),
                    (x1 - 30, y0 + 30, (0, 1, 0)),
                    (x0 + 30, y1 - 30, (0, 0, 1)),
                    (x1 - 30, y1 - 30, (1, 1, 0)),
                )
                for x, y, color in marks:
                    page.draw_rect(fitz.Rect(x - 12, y - 12, x + 12, y + 12),
                                   color=None, fill=color)
                page.insert_text((x0 + 55, y0 + 100), "LEFT COLUMN")
                page.insert_text((x0 + 300, y0 + 100), "RIGHT COLUMN")
                page.draw_rect(fitz.Rect(x0 + 55, y0 + 120, x0 + 200, y0 + 160),
                               color=None, fill=(1, 0.5, 0))
                page.draw_rect(fitz.Rect(x1 - 200, y0 + 120, x1 - 55, y0 + 160),
                               color=None, fill=(0, 1, 1))
                page.draw_rect(fitz.Rect(x0 + 50, y0 + 200, x1 - 50, y0 + 240),
                               color=None, fill=(1, 0, 1))
                if cropped:
                    page.set_cropbox(fitz.Rect(box))
                page.set_rotation(rotation)
            document.save(path)

    def run_cli(self, pages="1", *options, pdf=None, out=None):
        environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(SCRIPT),
             str(pdf or self.pdf), pages, "--out", str(out or self.out), *options],
            capture_output=True, text=True, encoding="utf-8", env=environment,
            timeout=30,
        )

    def assert_success(self, result):
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def assert_pixel(self, image, x, y, expected):
        actual = image.pixel(x, y)[:3]
        for value, target in zip(actual, expected):
            self.assertLessEqual(abs(value - target), 3, (actual, expected))

    def test_clip_renders_requested_pixels(self):
        result = self.run_cli("1", "--clip", "20,20,40,40", "--dpi", "72")
        self.assert_success(result)
        images = list(self.out.glob("*.png"))
        self.assertEqual(len(images), 1)
        image = fitz.Pixmap(str(images[0]))
        self.assertEqual((image.width, image.height), (20, 20))
        self.assert_pixel(image, 10, 10, (255, 0, 0))

    def test_crop_pixels_respect_rotation_and_cropbox(self):
        # Explicit geometry expectations, not page.rotation_matrix or a second crop.
        for cropped in (False, True):
            width, height = (520, 680) if cropped else (600, 800)
            for rotation in (0, 90, 180, 270):
                with self.subTest(cropped=cropped, rotation=rotation):
                    source = self.root / f"rotation-{rotation}-{cropped}.pdf"
                    self.make_pdf(source, rotation=rotation, cropped=cropped)
                    corners = (
                        (30, 30, (255, 0, 0)),
                        (width - 30, 30, (0, 255, 0)),
                        (30, height - 30, (0, 0, 255)),
                        (width - 30, height - 30, (255, 255, 0)),
                    )
                    for number, (x, y, color) in enumerate(corners):
                        if rotation == 90:
                            x, y = height - y, x
                        elif rotation == 180:
                            x, y = width - x, height - y
                        elif rotation == 270:
                            x, y = y, width - x
                        clip = f"{x-8},{y-6},{x+8},{y+6}"
                        output = self.root / f"crop-{cropped}-{rotation}-{number}"
                        result = self.run_cli("1", "--clip", clip, "--dpi", "72",
                                              pdf=source, out=output)
                        self.assert_success(result)
                        image = fitz.Pixmap(str(next(output.glob("*.png"))))
                        self.assertEqual((image.width, image.height), (16, 12))
                        self.assert_pixel(image, 8, 6, color)

    def test_cross_column_region_and_dpi_scaling(self):
        for dpi in (72, 144):
            with self.subTest(dpi=dpi):
                output = self.root / f"span-{dpi}"
                result = self.run_cli("1", "--clip", "40,190,560,250",
                                      "--dpi", str(dpi), out=output)
                self.assert_success(result)
                image = fitz.Pixmap(str(next(output.glob("*.png"))))
                scale = dpi // 72
                self.assertEqual((image.width, image.height), (520 * scale, 60 * scale))
                for x in (30, 260, 490):
                    self.assert_pixel(image, x * scale, 30 * scale, (255, 0, 255))
                self.assert_pixel(image, 5 * scale, 5 * scale, (255, 255, 255))

    def test_distinct_single_column_regions(self):
        for clip, color in (("60,125,190,155", (255, 127, 0)),
                            ("410,125,540,155", (0, 255, 255))):
            with self.subTest(clip=clip):
                output = self.root / f"column-{clip.split(',')[0]}"
                result = self.run_cli("1", "--clip", clip, "--dpi", "72", out=output)
                self.assert_success(result)
                image = fitz.Pixmap(str(next(output.glob("*.png"))))
                self.assertEqual((image.width, image.height), (130, 30))
                self.assert_pixel(image, 65, 15, color)

    def test_raster_only_region(self):
        source = self.root / "raster.pdf"
        # PPM image: left half red, right half blue. No image-processing dependency.
        samples = ((b"\xff\x00\x00" * 2 + b"\x00\x00\xff" * 2) * 4)
        ppm = b"P6\n4 4\n255\n" + samples
        with fitz.open() as document:
            page = document.new_page(width=200, height=200)
            page.insert_image(page.rect, stream=ppm)
            document.save(source)
        result = self.run_cli("1", "--clip", "120,30,170,80", "--dpi", "72", pdf=source)
        self.assert_success(result)
        image = fitz.Pixmap(str(next(self.out.glob("*.png"))))
        self.assertEqual((image.width, image.height), (50, 50))
        self.assert_pixel(image, 25, 25, (0, 0, 255))
        self.assertIn("Almost no text layer", result.stdout)

    def test_valid_old_multipage_usage_and_source_unchanged(self):
        source = self.root / "two-pages.pdf"
        self.make_pdf(source, pages=2)
        before = hashlib.sha256(source.read_bytes()).digest()
        result = self.run_cli("1, 2", pdf=source)
        self.assert_success(result)
        self.assertEqual({p.name for p in self.out.glob("*.png")},
                         {"two-pages_p1.png", "two-pages_p2.png"})
        image = fitz.Pixmap(str(self.out / "two-pages_p1.png"))
        self.assertEqual((image.width, image.height), (1250, 1667))
        self.assertIn(str(self.out.resolve()), result.stdout)
        self.assertIn("DPI=150", result.stdout)
        self.assertIn("full page", result.stdout)
        self.assertEqual(hashlib.sha256(source.read_bytes()).digest(), before)

    def test_invalid_arguments_create_no_output(self):
        cases = [
            ("1", "--clip=0,0,0,10"),
            ("1", "--clip=20,0,10,20"),
            ("1", "--clip=0,20,10,10"),
            ("1", "--clip=-1,0,10,10"),
            ("1", "--clip=0,0,601,10"),
            ("1", "--clip=0,0,10,801"),
            ("1", "--clip=nan,0,10,10"),
            ("1", "--clip=0,0,inf,10"),
            ("1", "--clip=0,0,10"),
            ("1", "--clip=a,0,10,10"),
            ("1,1", "--clip=0,0,10,10"),
            ("1", "--dpi", "0"),
            ("1", "--dpi", "-2"),
            ("",), (" ",), (",",), ("1,,1",), ("one",),
            ("0",), ("-1",), ("2",), ("1,2",),
        ]
        for arguments in cases:
            with self.subTest(arguments=arguments):
                result = self.run_cli(*arguments)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse(self.out.exists(), result.stdout + result.stderr)

    def test_clip_out_of_bounds_uses_displayed_dimensions(self):
        source = self.root / "rotated-cropbox.pdf"
        self.make_pdf(source, rotation=90, cropped=True)
        result = self.run_cli("1", "--clip=0,0,681,100", pdf=source)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.out.exists())

    def test_existing_files_repeated_runs_and_same_basename_are_safe(self):
        self.out.mkdir()
        sentinel = self.out / f"{self.pdf.stem}_p1.png"
        sentinel.write_bytes(b"existing file must survive")
        self.assert_success(self.run_cli())
        self.assert_success(self.run_cli())
        self.assertEqual(sentinel.read_bytes(), b"existing file must survive")
        sibling = self.root / "other"
        sibling.mkdir()
        other_pdf = sibling / self.pdf.name
        self.make_pdf(other_pdf, red=(0, 1, 1))
        self.assert_success(self.run_cli(pdf=other_pdf))
        files = list(self.out.glob("*.png"))
        self.assertEqual(len(files), 4)
        for source, expected in ((self.pdf, (255, 0, 0)), (other_pdf, (0, 255, 255))):
            before = hashlib.sha256(source.read_bytes()).digest()
            self.assert_success(self.run_cli("1", "--clip", "20,20,40,40",
                                             "--dpi", "72", pdf=source))
            self.assertEqual(hashlib.sha256(source.read_bytes()).digest(), before)
        crops = sorted(self.out.glob("*crop*.png"))
        self.assertEqual(len(crops), 2)
        observed = {fitz.Pixmap(str(p)).pixel(10, 10)[:3] for p in crops}
        self.assertEqual(observed, {(255, 0, 0), (0, 255, 255)})
        preserved = {p: p.read_bytes() for p in self.out.iterdir()}
        self.assert_success(self.run_cli("1", "--clip", "20,20,40,40", "--dpi", "72"))
        for path, contents in preserved.items():
            self.assertEqual(path.read_bytes(), contents)

    def test_output_directory_failure_is_clear(self):
        blocked = self.root / "not-a-directory"
        blocked.write_text("preserve", encoding="utf-8")
        result = self.run_cli(out=blocked / "child")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("output", result.stderr.lower())
        self.assertNotIn("Traceback", result.stderr)
        self.assertEqual(blocked.read_text(encoding="utf-8"), "preserve")

    def test_missing_or_invalid_source_creates_no_output(self):
        invalid = self.root / "invalid.pdf"
        invalid.write_bytes(b"not a PDF")
        for source in (self.root / "missing.pdf", invalid):
            with self.subTest(source=source):
                result = self.run_cli(pdf=source)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Cannot open PDF", result.stderr)
                self.assertFalse(self.out.exists())


if __name__ == "__main__":
    unittest.main()
