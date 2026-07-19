from pathlib import Path
import pymupdf


def extract_text_from_pdf(pdf_source) -> str:
    """
    Extract text from a PDF.

    Accepts:
    - pathlib.Path
    - Streamlit UploadedFile
    """

    if isinstance(pdf_source, Path):
        document = pymupdf.open(pdf_source)
    else:
        document = pymupdf.open(stream=pdf_source.read(), filetype="pdf")

    pages = []

    for page in document:
        pages.append(page.get_text())

    document.close()

    return " ".join(pages)