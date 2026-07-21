import fitz

from .pdf_extractor import extract_page_text as pdf_extract
from .ocr_extractor import extract_page_text as ocr_extract


def extract_resume(file_bytes: bytes):

    doc = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    text = ""

    ocr_pages = 0

    for index, page in enumerate(doc):

        page_text = pdf_extract(page)

        if page_text:

            print(f"Page {index+1}: PDF extraction")

            text += page_text + "\n"

        else:

            print(f"Page {index+1}: OCR")

            page_text = ocr_extract(page)

            text += page_text + "\n"

            ocr_pages += 1

    extraction_method = (
        "pdf"
        if ocr_pages == 0
        else "hybrid"
        if ocr_pages < len(doc)
        else "ocr"
    )

    return {
        "text": text,
        "page_count": len(doc),
        "ocr_pages": ocr_pages,
        "extraction_method": extraction_method
    }