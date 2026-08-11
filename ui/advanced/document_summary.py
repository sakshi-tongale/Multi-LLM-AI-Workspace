import streamlit as st

from tools.advanced.pdf_loader import load_pdf
from llms.gemini_client import ask_gemini
from utils.file_exporter import export_to_txt, export_to_docx


def document_summarizer_page(model=None):

    st.title("📄 AI Document Summarizer")

    uploaded_file = st.file_uploader(
        "Upload PDF Document",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    # ---------------- Save Uploaded PDF ---------------- #

    temp_path = "temp_summary.pdf"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    # ---------------- Read PDF ---------------- #

    with st.spinner("Reading PDF..."):

        text = load_pdf(temp_path)

    if not text.strip():

        st.error("❌ No text found in the PDF.")

        return

    st.success("✅ PDF Loaded Successfully!")

    st.info(f"📄 Extracted approximately {len(text):,} characters.")

    # ---------------- Generate Summary ---------------- #

    if st.button("🚀 Generate Summary", use_container_width=True):

        prompt = f"""
You are an AI Document Summarizer.

Read the document below and provide:

1. A short summary (4–6 sentences)

2. Main topics covered

3. Key points

4. Important conclusions

Document:

{text}
"""

        with st.spinner("Generating Summary..."):

            summary = ask_gemini(prompt)

        st.session_state.document_summary = summary

    # ---------------- Display ---------------- #

    if "document_summary" in st.session_state:

        st.success("✅ Summary Generated Successfully!")

        st.markdown("## 📄 Document Summary")

        st.markdown(st.session_state.document_summary)

        st.divider()

        st.subheader("Export Summary")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.document_summary,
                    "document_summary"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.document_summary,
                    "document_summary"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")