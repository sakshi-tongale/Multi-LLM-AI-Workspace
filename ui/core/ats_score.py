import streamlit as st
import tempfile
import os

from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model


def ats_score_page(model):

    st.title("📊 ATS Score Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        if st.button("📊 Calculate ATS Score", use_container_width=True):

            with st.spinner("Calculating ATS Score..."):

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
You are an expert ATS (Applicant Tracking System) Resume Reviewer.

Analyze the following resume.

Evaluate it based on:

1. Contact Information
2. Professional Summary
3. Skills
4. Work Experience
5. Projects
6. Education
7. Keywords & Technologies

Return the result in exactly this format:

ATS Score: XX/100

Section Scores:
- Contact Information:
- Professional Summary:
- Skills:
- Work Experience:
- Projects:
- Education:
- Keywords:

Strengths:
- ...

Weaknesses:
- ...

Missing Keywords:
- ...

Suggestions:
- ...

Resume:

{resume_text}
"""

                response = ask_model(model, prompt)

            st.success("ATS Analysis Complete!")

            st.divider()

            st.markdown(response)