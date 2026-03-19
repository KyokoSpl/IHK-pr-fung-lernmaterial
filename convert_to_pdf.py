#!/usr/bin/env python3
"""
Converts all Markdown files in the workspace subfolders to PDF.
Each .pdf is placed next to its source .md file.

Dependencies:
    pip install markdown2 weasyprint

Usage:
    python convert_to_pdf.py
"""

import os
import sys
from pathlib import Path

try:
    import markdown2
except ImportError:
    sys.exit("Missing dependency: pip install markdown2")

try:
    from weasyprint import HTML
except ImportError:
    sys.exit("Missing dependency: pip install weasyprint")


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<style>
    body {{
        font-family: "Noto Sans", "DejaVu Sans", Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.5;
        max-width: 190mm;
        margin: 15mm auto;
        color: #1a1a1a;
    }}
    h1 {{ font-size: 20pt; margin-top: 0; border-bottom: 2px solid #2c3e50; padding-bottom: 6pt; }}
    h2 {{ font-size: 16pt; color: #2c3e50; margin-top: 18pt; }}
    h3 {{ font-size: 13pt; color: #34495e; margin-top: 14pt; }}
    code {{
        font-family: "Noto Mono", "DejaVu Sans Mono", monospace;
        background: #f4f4f4;
        padding: 1px 4px;
        border-radius: 3px;
        font-size: 10pt;
    }}
    pre {{
        background: #f4f4f4;
        padding: 10px 14px;
        border-radius: 4px;
        overflow-x: auto;
        font-size: 9.5pt;
        line-height: 1.4;
    }}
    pre code {{
        background: none;
        padding: 0;
    }}
    table {{
        border-collapse: collapse;
        width: 100%;
        margin: 12px 0;
    }}
    th, td {{
        border: 1px solid #ccc;
        padding: 6px 10px;
        text-align: left;
    }}
    th {{
        background: #ecf0f1;
        font-weight: bold;
    }}
    blockquote {{
        border-left: 4px solid #2c3e50;
        margin: 12px 0;
        padding: 6px 14px;
        color: #555;
        background: #fafafa;
    }}
    ul, ol {{ padding-left: 24px; }}
    li {{ margin-bottom: 4px; }}
    strong {{ color: #2c3e50; }}
    @page {{
        size: A4;
        margin: 20mm 15mm;
    }}
</style>
</head>
<body>
{content}
</body>
</html>
"""

EXTRAS = [
    "fenced-code-blocks",
    "tables",
    "header-ids",
    "strike",
    "task_list",
    "cuddled-lists",
    "code-friendly",
]


def convert_md_to_pdf(md_path: Path) -> bool:
    """Convert a single markdown file to PDF. Returns True on success."""
    pdf_path = md_path.with_suffix(".pdf")
    try:
        md_text = md_path.read_text(encoding="utf-8")
        html_body = markdown2.markdown(md_text, extras=EXTRAS)
        full_html = HTML_TEMPLATE.format(content=html_body)
        HTML(string=full_html).write_pdf(str(pdf_path))
        return True
    except Exception as e:
        print(f"  ERROR: {md_path} -> {e}", file=sys.stderr)
        return False


def main():
    root = Path(__file__).resolve().parent
    md_files = sorted(root.rglob("*.md"))

    if not md_files:
        print("No markdown files found.")
        return

    print(f"Found {len(md_files)} markdown files. Converting to PDF...\n")

    success = 0
    failed = 0

    for md_file in md_files:
        rel = md_file.relative_to(root)
        print(f"  [{success + failed + 1}/{len(md_files)}] {rel}")
        if convert_md_to_pdf(md_file):
            success += 1
        else:
            failed += 1

    print(f"\nDone: {success} converted, {failed} failed.")


if __name__ == "__main__":
    main()
