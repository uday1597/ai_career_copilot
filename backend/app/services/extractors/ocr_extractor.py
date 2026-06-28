import fitz
import numpy as np
import pytesseract

from PIL import Image


def extract_page_text(page) -> str:
    """
    Extract text from a scanned PDF page using OCR.
    """

    pix = page.get_pixmap(
        matrix=fitz.Matrix(2, 2)
    )

    img = Image.fromarray(
        np.frombuffer(
            pix.samples,
            dtype=np.uint8
        ).reshape(
            pix.height,
            pix.width,
            pix.n
        )
    )

    return pytesseract.image_to_string(img).strip()