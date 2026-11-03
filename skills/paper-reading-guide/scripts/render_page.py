#!/usr/bin/env python3
"""
Render selected PDF pages as PNGs for inspecting curves, heatmaps, network
diagrams, and other visual content unavailable from text alone. Use caption page
numbers from extract_outline.py, then actually inspect the rendered images.

Usage:
    python render_page.py paper.pdf 5              # Render page 5.
    python render_page.py paper.pdf 5,7,8          # Render multiple pages.
    python render_page.py paper.pdf 5 --dpi 200    # Resolution; default is 150.
    python render_page.py paper.pdf 5 --out figs   # Output directory; default is ./figures.
    python render_page.py paper.pdf 5 --clip 30,40,300,220 --dpi 200 --out figs

--clip takes one page and displayed-page coordinates in PDF points (72 per inch),
with origin at the visible page's top-left after rotation/CropBox. It is independent
of DPI. Text/search rectangles use unrotated coordinates: convert them with
page.rotation_matrix before supplying a displayed clip; do not rotate it twice.

Dependency: PyMuPDF -> pip install pymupdf
Output: <pdf-name>_p<page>.png, or <pdf-name>_p<page>_crop_<coordinates>.png.
Collisions gain _2, _3, ... using exclusive creation; existing files are never
overwritten. All page/clip/DPI arguments are checked before output creation.
Invalid pages are errors, rather than skipped. Files already exported remain on
later filesystem failure; multi-page output is not an atomic transaction.
"""
import sys
import os
import argparse
import math
from pathlib import Path


def save_unique_png(pixmap, output):
    """Create a new PNG exclusively, including when another process wins a name."""
    contents = pixmap.tobytes("png")
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
            raise OSError(f"writing {candidate} failed; an incomplete file may remain: {exc}") from exc
        return candidate


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf")
    ap.add_argument("pages", help="1-based page numbers, comma-separated: 5 or 5,7,8")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--out", default="figures")
    ap.add_argument("--clip", help="one page only: x0,y0,x1,y1 in displayed-page PDF points")
    args = ap.parse_args()

    if args.dpi <= 0:
        ap.error("DPI must be a positive integer")
    try:
        tokens = [token.strip() for token in args.pages.split(",")]
        if not all(tokens):
            raise ValueError
        pages = [int(token) for token in tokens]
    except ValueError:
        ap.error("Invalid page format; use nonempty 1-based page numbers such as 5 or 5,7,8")

    coordinates = None
    if args.clip is not None:
        if len(pages) != 1:
            ap.error("--clip requires exactly one page")
        try:
            coordinates = tuple(float(value) for value in args.clip.split(","))
        except ValueError:
            ap.error("--clip requires four finite numbers: x0,y0,x1,y1")
        if len(coordinates) != 4 or not all(math.isfinite(value) for value in coordinates):
            ap.error("--clip requires four finite numbers: x0,y0,x1,y1")
        x0, y0, x1, y1 = coordinates
        if x0 >= x1 or y0 >= y1:
            ap.error("--clip must have positive width and height, with x0 < x1 and y0 < y1")

    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("PyMuPDF is missing. Install it with: pip install pymupdf")

    try:
        doc = fitz.open(args.pdf)
    except Exception as e:
        sys.exit(f"Cannot open PDF: {e}")

    with doc:
        if doc.needs_pass:
            sys.exit("Cannot render PDF: a password is required")
        for p in pages:
            if p < 1 or p > doc.page_count:
                ap.error(f"Page {p} is outside range 1–{doc.page_count}; no output created")
        clip = fitz.Rect(coordinates) if coordinates is not None else None
        if clip is not None:
            bounds = doc[pages[0] - 1].rect
            if not bounds.contains(clip):
                ap.error(f"--clip is outside displayed page bounds {tuple(bounds)}; no output created")

        try:
            output_dir = Path(args.out).resolve()
            output_dir.mkdir(parents=True, exist_ok=True)
        except (OSError, ValueError) as exc:
            sys.exit(f"Cannot create output directory: {exc}")
        base = os.path.splitext(os.path.basename(args.pdf))[0]
        mat = fitz.Matrix(args.dpi / 72.0, args.dpi / 72.0)
        region = "_crop_" + "_".join(str(value) for value in coordinates) if clip is not None else ""

        for p in pages:
            try:
                page = doc[p - 1]
                text_len = len(page.get_text("text").strip())
                # get_pixmap clips in displayed coordinates and respects page rotation.
                pix = page.get_pixmap(matrix=mat, clip=clip)
                out_path = save_unique_png(pix, output_dir / f"{base}_p{p}{region}.png")
            except Exception as exc:
                sys.exit(f"Cannot export PDF page {p}: {exc}; earlier exports are retained")
            area = f"clip={coordinates}" if clip is not None else "full page"
            flag = "  ⚠ Almost no text layer; possible scan/image page (text extraction may be empty)" if text_len < 40 else ""
            print(f"  Exported: {out_path}  (page={p}, {area}, DPI={args.dpi}, {pix.width}x{pix.height}, page text characters≈{text_len}){flag}")

    print("\nTip: inspect the exported PNGs yourself or with a vision-capable model to read visual details.")


if __name__ == "__main__":
    main()
