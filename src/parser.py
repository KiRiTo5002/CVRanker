from pathlib import Path

import pymupdf


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""

    document = pymupdf.open(pdf_path)

    pages = []

    for page in document:
        page_text = page.get_text()
        pages.append(page_text)

    document.close()

    return " ".join(pages)