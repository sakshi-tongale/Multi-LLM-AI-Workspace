from tools.advanced.pdf_loader import load_pdf
from tools.advanced.text_splitter import split_text
from tools.advanced.vector_store import (
    create_vector_store,
    search_vector_store
)
from llms.gemini_client import ask_gemini


def prepare_pdf(pdf_path):
    """
    Load the PDF, split it into chunks,
    and create the FAISS vector store.
    """

    # Load PDF
    text = load_pdf(pdf_path)

    # Split text into chunks
    chunks = split_text(text)

    # Create FAISS vector store
    index, chunks = create_vector_store(chunks)

    return index, chunks


def retrieve_context(index, chunks, question):
    """
    Search the vector store and return
    the most relevant chunks as context.
    """

    results = search_vector_store(index, chunks, question)

    context = "\n\n".join(results)

    return context


def ask_pdf(question, index, chunks):
    """
    Complete RAG Pipeline

    1. Retrieve relevant chunks
    2. Create prompt
    3. Ask Gemini
    4. Return final answer
    """

    # Retrieve context from vector database
    context = retrieve_context(index, chunks, question)

    # Create RAG Prompt
    prompt = f"""
You are an AI assistant that answers questions ONLY from the provided PDF context.

Instructions:
- Answer only using the context below.
- If the answer is not found in the context, reply:
  "I couldn't find that information in the PDF."
- Keep the answer clear and concise.

======================
PDF Context
======================

{context}

======================
User Question
======================

{question}

======================
Answer
======================
"""

    # Ask Gemini
    answer = ask_gemini(prompt)

    return answer