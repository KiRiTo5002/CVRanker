from pathlib import Path
import pymupdf


def extract_text_from_pdf(pdf_path: Path) -> str:
    doc = pymupdf.open(pdf_path)
    pages = []
    for page in doc:
        page = page.get_text()
        pages.append(page)
    text = " ".join(pages)
    doc.close()
    return text
