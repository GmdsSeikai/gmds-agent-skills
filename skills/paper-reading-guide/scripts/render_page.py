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

Dependency: PyMuPDF -> pip install pymupdf
Output: figures/<pdf-name>_p<page>.png and a text-character count for each page
to help identify pages with little or no text layer.
"""
import sys
import os
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("pages", help="1-based page numbers, comma-separated: 5 or 5,7,8")
    ap.add_argument("--dpi", type=int, default=150)
    ap.add_argument("--out", default="figures")
    args = ap.parse_args()

    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("PyMuPDF is missing. Install it with: pip install pymupdf")

    try:
        doc = fitz.open(args.pdf)
    except Exception as e:
        sys.exit(f"Cannot open PDF: {e}")

    try:
        pages = [int(p) for p in args.pages.replace(" ", "").split(",") if p]
    except ValueError:
        sys.exit("Invalid page format; use 5 or 5,7,8")

    os.makedirs(args.out, exist_ok=True)
    base = os.path.splitext(os.path.basename(args.pdf))[0]
    zoom = args.dpi / 72.0
    mat = fitz.Matrix(zoom, zoom)

    for p in pages:
        if p < 1 or p > doc.page_count:
            print(f"  Skipping page {p} (outside range 1–{doc.page_count})")
            continue
        page = doc[p - 1]
        text_len = len(page.get_text("text").strip())
        pix = page.get_pixmap(matrix=mat)
        out_path = os.path.join(args.out, f"{base}_p{p}.png")
        pix.save(out_path)
        flag = "  ⚠ Almost no text layer; possible scan/image page (text extraction may be empty)" if text_len < 40 else ""
        print(f"  Exported: {out_path}  ({pix.width}x{pix.height}, text characters≈{text_len}){flag}")

    print("\nTip: inspect the exported PNGs yourself or with a vision-capable model to read visual details.")


if __name__ == "__main__":
    main()
