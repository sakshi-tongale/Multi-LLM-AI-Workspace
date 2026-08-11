import streamlit as st

from tools.advanced.pdf_loader import load_pdf
from tools.advanced.text_splitter import split_text
from tools.advanced.vector_store import (
    create_vector_store,
    search_vector_store
)

from llms.gemini_client import ask_gemini
from utils.file_exporter import export_to_txt, export_to_docx


def document_qa_page(model=None):

    st.title("❓ AI Document Q&A")

    uploaded_file = st.file_uploader(
        "Upload PDF Document",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    # Save uploaded PDF
    temp_path = "temp_document_qa.pdf"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Read PDF
    with st.spinner("Reading PDF..."):

        text = load_pdf(temp_path)

    if not text.strip():

        st.error("❌ No text found in the PDF.")

        return

    st.success("✅ PDF Loaded Successfully!")

    question = st.text_input(
        "Ask a question about the document"
    )

    if st.button("🚀 Get Answer", use_container_width=True):

        if question.strip() == "":
            st.warning("Please enter a question.")
            st.stop()

        with st.spinner("Searching document..."):

            chunks = split_text(text)

            index, chunks = create_vector_store(chunks)

            results = search_vector_store(
                index,
                chunks,
                question
            )

            context = "\n\n".join(results)

            prompt = f"""
You are an AI Document Question Answering Assistant.

Answer ONLY using the document context below.

If the answer is not found, reply:

"I couldn't find that information in the document."

Document Context:

{context}

Question:

{question}
"""

            answer = ask_gemini(prompt)

        st.session_state.document_answer = answer

    if "document_answer" in st.session_state:

        st.success("✅ Answer Generated!")

        st.markdown("## Answer")

        st.markdown(st.session_state.document_answer)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "📄 Save as TXT",
                use_container_width=True
            ):

                path = export_to_txt(
                    st.session_state.document_answer,
                    "document_answer"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button(
                "📝 Save as DOCX",
                use_container_width=True
            ):

                path = export_to_docx(
                    st.session_state.document_answer,
                    "document_answer"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")