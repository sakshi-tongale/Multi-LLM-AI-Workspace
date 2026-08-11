from tools.advanced.pdf_loader import load_pdf
from tools.advanced.text_splitter import split_text
from tools.advanced.vector_store import (
    create_vector_store,
    search_vector_store
)
from llms.gemini_client import ask_gemini


def document_qa(model=None):
    """
    Ask one question from a PDF document.
    """

    # Ask for PDF path
    pdf_path = input("\nEnter PDF path: ")

    print("\nReading PDF...\n")

    # Load PDF
    text = load_pdf(pdf_path)

    # Split PDF into chunks
    chunks = split_text(text)

    # Create FAISS Vector Store
    index, chunks = create_vector_store(chunks)

    print("\n✅ Document Loaded Successfully!")

    # Ask one question
    question = input("\nEnter your question: ")

    print("\nSearching Document...\n")

    # Retrieve relevant chunks
    results = search_vector_store(index, chunks, question)

    # Convert retrieved chunks into context
    context = "\n\n".join(results)

    # Create prompt
    prompt = f"""
You are an AI Document Question Answering Assistant.

Answer the user's question ONLY using the information provided in the document context.

Rules:
- If the answer is found in the context, answer clearly.
- If the answer is NOT found, reply:
"I couldn't find that information in the document."
- Do not make up information.

=========================
Document Context
=========================

{context}

=========================
Question
=========================

{question}

=========================
Answer
=========================
"""

    print("Generating Answer...\n")

    # Ask Gemini
    answer = ask_gemini(prompt)

    print("=" * 60)
    print("Document Answer")
    print("=" * 60)
    print(answer)