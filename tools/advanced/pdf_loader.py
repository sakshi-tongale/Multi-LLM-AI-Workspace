from pypdf import PdfReader


def load_pdf(pdf_path):
    """
    Load a PDF and return all extracted text.
    """

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text