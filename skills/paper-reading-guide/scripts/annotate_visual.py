#!/usr/bin/env python3
"""Compose a checked PNG crop with vector teaching callouts using PyMuPDF.

See references/visual-annotations.md for the version-1 JSON contract. Coordinates
are source-image pixels; labels live in added margins. No PDF is opened or saved.
"""
import argparse
import json
import math
from pathlib import Path
import sys


def write_unique(contents, output):
    """Exclusive creation also protects against concurrent filename collisions."""
    number = 1
    while True:
        candidate = output if number == 1 else output.with_name(
            f"{output.stem}_{number}{output.suffix}"
        )
        try:
            stream = candidate.open("xb")
        except FileExistsError:
            number += 1
            continue
        try:
            with stream:
                stream.write(contents)
        except OSError as exc:
            raise OSError(f"writing {candidate} failed; an incomplete file may remain") from exc
        return candidate


def point(value, name):
    if (not isinstance(value, list) or len(value) != 2
            or any(type(v) not in (int, float) or not math.isfinite(v) for v in value)):
        raise ValueError(f"{name} must contain two finite numbers")
    return tuple(value)


def text(value, name, font):
    if not isinstance(value, str) or not value.strip() or any(c.isspace() and c != " " for c in value):
        raise ValueError(f"{name} must be nonempty single-line text")
    missing = [f"U+{ord(c):04X}" for c in value if not font.has_glyph(ord(c), fallback=False)]
    if missing:
        raise ValueError(f"font lacks glyphs for {name}: {', '.join(sorted(set(missing)))}; supply --font")
    return value


def compose(source_bytes, spec, padding, size, font, fitz):
    """Validate all geometry and glyphs, then render without filesystem effects."""
    if not source_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("source must be a readable PNG crop")
    source = fitz.Pixmap(source_bytes)
    width, height = source.width, source.height
    if source.alpha or source.n != 3:
        raise ValueError("source must be an opaque RGB PNG; render a clean RGB crop first")
    if not isinstance(spec, dict) or set(spec) != {"version", "title", "callouts"} or type(spec["version"]) is not int or spec["version"] != 1:
        raise ValueError("spec requires exactly version=1, title and callouts")
    title = text(spec["title"], "title", font)
    callouts = spec["callouts"]
    if not isinstance(callouts, list) or not callouts:
        raise ValueError("callouts must be a nonempty list")
    canvas = fitz.Rect(-padding, -padding, width + padding, height + padding)
    original = fitz.Rect(0, 0, width, height)
    line_height = size * (font.ascender - font.descender)
    title_box = fitz.Rect(-padding + 16, -padding + 12,
                          -padding + 16 + font.text_length(title, fontsize=size),
                          -padding + 12 + line_height)
    if not canvas.contains(title_box) or title_box.intersects(original):
        raise ValueError("title does not fit the top margin; shorten it or increase --padding")
    prepared = []
    boxes = [title_box]
    for index, callout in enumerate(callouts, 1):
        if not isinstance(callout, dict) or not {"text", "target", "label"} <= set(callout) or set(callout) - {"text", "target", "label", "via"}:
            raise ValueError(f"callout {index} requires text, target, label and optional via")
        label = text(callout["text"], f"callout {index}", font)
        x, y = point(callout["label"], "label")
        target = point(callout["target"], "target")
        if not (0 <= target[0] < width and 0 <= target[1] < height):
            raise ValueError(f"callout {index} target is outside the source image")
        box = fitz.Rect(x, y, x + font.text_length(label, fontsize=size), y + line_height)
        if not canvas.contains(box) or box.intersects(original):
            raise ValueError(f"callout {index} label must fit wholly in the added margin")
        if any(box.intersects(other) for other in boxes):
            raise ValueError(f"callout {index} label overlaps another label or title")
        via = callout.get("via", [])
        if not isinstance(via, list):
            raise ValueError("via must be a list of points")
        bends = [point(value, "via") for value in via]
        if any(not (canvas.x0 <= a <= canvas.x1 and canvas.y0 <= b <= canvas.y1) for a, b in bends):
            raise ValueError(f"callout {index} via point is outside the canvas")
        # A nearest-edge leader avoids drawing through its own text.
        start = (min(max(target[0], box.x0), box.x1),
                 min(max(target[1], box.y0), box.y1))
        prepared.append((label, box, [start, *bends, target]))
        boxes.append(box)

    offset = fitz.Point(padding, padding)
    with fitz.open() as document:
        page = document.new_page(width=canvas.width, height=canvas.height)
        page.insert_image(original + (padding, padding, padding, padding), stream=source_bytes)
        page.insert_font(fontname="labels", fontbuffer=font.buffer)
        ink = (0.05, 0.3, 0.65)
        for label, box in [(title, title_box), *[(label, box) for label, box, _ in prepared]]:
            page.insert_text(fitz.Point(box.x0, box.y0 + size * font.ascender) + offset,
                             label, fontsize=size, fontname="labels", color=ink)
        for _, _, points in prepared:
            page.draw_polyline([fitz.Point(p) + offset for p in points], color=ink, width=1)
        return page.get_pixmap(alpha=False).tobytes("png"), (width, height)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", help="checked opaque RGB PNG crop")
    parser.add_argument("spec", help="UTF-8 version-1 callout JSON")
    parser.add_argument("--out", required=True, help="task artifact directory")
    parser.add_argument("--padding", type=int, default=200, help="margin on each side, in image pixels")
    parser.add_argument("--font-size", type=int, default=18, help="label size in image pixels")
    parser.add_argument("--font", help="caller-supplied font file; default: PyMuPDF bundled CJK font")
    args = parser.parse_args()
    if args.padding <= 0 or args.font_size <= 0:
        parser.error("--padding and --font-size must be positive integers")
    try:
        import fitz
    except ImportError:
        sys.exit("PyMuPDF is unavailable; use the clean original with a text explanation")
    try:
        font = fitz.Font(fontfile=args.font) if args.font else fitz.Font("cjk")
        source_path = Path(args.image)
        source_bytes = source_path.read_bytes()
        spec = json.loads(Path(args.spec).read_text(encoding="utf-8-sig"))
        annotated, dimensions = compose(source_bytes, spec, args.padding, args.font_size, font, fitz)
    except Exception as exc:
        sys.exit(f"Cannot prepare teaching annotation: {exc}; no output created")
    try:
        output_dir = Path(args.out).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        clean = write_unique(source_bytes, output_dir / f"{source_path.stem}.original.png")
        marked = write_unique(annotated, output_dir / f"{source_path.stem}.annotated.png")
    except Exception as exc:
        sys.exit(f"Cannot export teaching annotation: {exc}; earlier exports are retained")
    print(f"Clean original: {clean}")
    print(f"Teaching annotation: {marked}")
    print(f"Source pixels: {dimensions[0]}x{dimensions[1]}; offset=({args.padding},{args.padding}); inspect labels and leader paths before sending")


if __name__ == "__main__":
    main()
