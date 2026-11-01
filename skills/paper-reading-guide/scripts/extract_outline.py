#!/usr/bin/env python3
"""
Extract heuristic section headings and figure/table captions for PDF navigation.
This lightweight outline does not replace reading the full paper.

Usage:
    python extract_outline.py path/to/paper.pdf
    python extract_outline.py path/to/paper.pdf --max-chars 1200

Dependency: PyMuPDF -> pip install pymupdf
Output: an abstract excerpt, candidate headings, and caption lines with page
numbers (for example, p7: Figure 4 ...). Pass those pages to render_page.py for
visual inspection. Text extraction cannot establish curve or heatmap details.
"""
import sys
import re
import argparse

CAPTION_RE = re.compile(r'^\s*(figure|fig\.?|table|图|表)\s*\d', re.IGNORECASE)
# Heading heuristic: short lines without a final period, matching heading patterns.
HEADING_RE = re.compile(
    r'^\s*(\d+(\.\d+)*\s+\S|abstract|introduction|related work|method|methodology|'
    r'experiment|experiments|results|discussion|conclusion|references|引言|摘要|'
    r'方法|实验|结果|讨论|结论|相关工作)',
    re.IGNORECASE,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--max-chars", type=int, default=1200,
                    help="Maximum characters in the abstract excerpt")
    args = ap.parse_args()

    try:
        import fitz  # PyMuPDF
    except ImportError:
        sys.exit("PyMuPDF is missing. Install it with: pip install pymupdf")

    try:
        doc = fitz.open(args.pdf)
    except Exception as e:
        sys.exit(f"Cannot open PDF: {e}")

    full_text = []
    headings = []
    captions = []

    for page_idx, page in enumerate(doc, start=1):
        text = page.get_text("text")
        full_text.append(text)
        for line in text.splitlines():
            s = line.strip()
            if not s:
                continue
            if CAPTION_RE.match(s):
                captions.append((page_idx, s[:160]))
            elif len(s) < 80 and not s.endswith(('.', '。', ',', '，')) and HEADING_RE.match(s):
                headings.append(s[:80])

    joined = "\n".join(full_text)

    # Take an excerpt after the English or Chinese abstract marker.
    abs = ""
    m = re.search(r'(abstract|摘要)', joined, re.IGNORECASE)
    if m:
        abs = joined[m.end(): m.end() + args.max_chars]
        abs = re.sub(r'\s+', ' ', abs).strip()

    print("=" * 60)
    print(f"File: {args.pdf}  ({doc.page_count} pages)")
    print("=" * 60)
    print("\n[Abstract excerpt]")
    print(abs if abs else "(Abstract not located; inspect the first page manually)")
    print("\n[Candidate section headings]")
    if headings:
        for h in dict.fromkeys(headings):   # Deduplicate while preserving order.
            print("  -", h)
    else:
        print("  (No headings extracted; possible scan or unusual layout)")
    print("\n[Figure / table caption lines, with page numbers]")
    if captions:
        seen = set()
        for page_no, cap in captions:
            key = (page_no, cap)
            if key in seen:
                continue
            seen.add(key)
            print(f"  p{page_no}: {cap}")
    else:
        print("  (No caption lines extracted)")
    print("\nTip: text extraction cannot verify curve or heatmap details. Render the pages above:")
    print(f"  python render_page.py \"{args.pdf}\" <page>")


if __name__ == "__main__":
    main()
