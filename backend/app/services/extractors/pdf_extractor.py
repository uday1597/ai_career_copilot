import fitz


def extract_page_text(page) -> str:
    """
    Extract text from a PDF page using native PDF extraction.
    """
    return page.get_text().strip()