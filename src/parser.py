from pathlib import Path

import pymupdf


def extract_text_from_pdf(pdf_source) -> str:
    """
    Extract all text from a PDF document.

    Args:
        pdf_source: A pathlib.Path or Streamlit UploadedFile.

    Returns:
        A single string containing the extracted text.
    """

    if isinstance(pdf_source, Path):
        document = pymupdf.open(pdf_source)
    else:
        document = pymupdf.open(
            stream=pdf_source.read(),
            filetype="pdf",
        )

    page_texts = []

    for page in document:
        page_texts.append(page.get_text())

    document.close()

    return " ".join(page_texts)