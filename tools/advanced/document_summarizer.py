from tools.advanced.pdf_loader import load_pdf
from llms.gemini_client import ask_gemini


def document_summarizer(model=None):
    """
    Summarize a PDF document using Gemini.
    """

    pdf_path = input("\nEnter PDF path: ")

    print("\nReading PDF...\n")

    text = load_pdf(pdf_path)

    if not text.strip():
        print("❌ No text found in the PDF.")
        return

    print("\nGenerating Summary...\n")

    prompt = f"""
You are an AI Document Summarizer.

Read the document below and provide:

1. A short summary (4-6 sentences)
2. Main topics covered
3. Key points
4. Important conclusions

Document:

{text}
"""

    summary = ask_gemini(prompt)

    print("=" * 60)
    print("Document Summary")
    print("=" * 60)
    print(summary)