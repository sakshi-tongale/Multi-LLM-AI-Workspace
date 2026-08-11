import streamlit as st
import tempfile
import os

from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model


def resume_analyzer_page(model):

    st.title("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("🚀 Analyze Resume", use_container_width=True):

            with st.spinner("Analyzing Resume..."):

                # Save uploaded PDF temporarily
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    pdf_path = tmp.name

                try:
                    resume_text = extract_text_from_pdf(pdf_path)

                except Exception as e:
                    st.error(f"Error reading PDF:\n\n{e}")
                    return

                finally:
                    if os.path.exists(pdf_path):
                        os.remove(pdf_path)

                prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume and provide:

1. ATS Score (out of 100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for Improvement

Resume:

{resume_text}
"""

                response = ask_model(model, prompt)

            st.success("Analysis Complete!")

            st.markdown("---")

            st.markdown(response)