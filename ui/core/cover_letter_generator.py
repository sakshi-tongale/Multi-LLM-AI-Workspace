import streamlit as st
import tempfile
import os

from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def cover_letter_generator_page(model):

    st.title("✉️ AI Cover Letter Generator")

    uploaded_file = st.file_uploader(
        "Upload Your Resume (PDF)",
        type=["pdf"]
    )

    job_title = st.text_input("Job Title")

    company_name = st.text_input("Company Name")

    job_description = st.text_area(
        "Job Description (Optional)",
        height=180
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate Cover Letter", use_container_width=True):

        if uploaded_file is None:
            st.warning("Please upload your resume.")
            return

        with st.spinner("Generating Cover Letter..."):

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
You are an expert career coach.

Using the resume below, write a professional cover letter.

Candidate Resume:
{resume_text}

Job Title:
{job_title}

Company:
{company_name}

Job Description:
{job_description}

Instructions:

- Keep it professional.
- Keep it to one page.
- Highlight relevant skills and projects.
- Mention enthusiasm for the company.
- End professionally.
"""

            response = ask_model(model, prompt)

            st.session_state.cover_letter = response

    # ---------------- Display ---------------- #

    if "cover_letter" in st.session_state:

        st.success("✅ Cover Letter Generated Successfully!")

        st.markdown("## Generated Cover Letter")

        st.markdown(st.session_state.cover_letter)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.cover_letter,
                    "cover_letter"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.cover_letter,
                    "cover_letter"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")