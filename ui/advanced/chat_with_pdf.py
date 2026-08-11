import streamlit as st

from tools.advanced.rag_pipeline import prepare_pdf, ask_pdf


def chat_with_pdf_page(model=None):

    st.title("📄 AI Chat with PDF")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    # Save uploaded PDF temporarily
    temp_path = "temp_uploaded_pdf.pdf"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # Prepare PDF only once
    if "pdf_index" not in st.session_state:

        with st.spinner("Processing PDF..."):

            index, chunks = prepare_pdf(temp_path)

        st.session_state.pdf_index = index
        st.session_state.pdf_chunks = chunks

        st.success("✅ PDF Loaded Successfully!")

    st.divider()

    question = st.text_input(
        "Ask a question about the PDF"
    )

    if st.button("🚀 Ask Question", use_container_width=True):

        if question.strip() == "":
            st.warning("Please enter a question.")
            return

        with st.spinner("Generating Answer..."):

            answer = ask_pdf(
                question,
                st.session_state.pdf_index,
                st.session_state.pdf_chunks
            )

        st.session_state.pdf_answer = answer

    # ---------------- Display ---------------- #

    if "pdf_answer" in st.session_state:

        st.success("✅ Answer Generated!")

        st.markdown("## Answer")

        st.markdown(st.session_state.pdf_answer)