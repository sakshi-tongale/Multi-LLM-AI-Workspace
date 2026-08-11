import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def code_reviewer_page(model):

    st.title("✅ AI Code Reviewer")

    language = st.selectbox(
        "Select Programming Language",
        [
            "Python",
            "Java",
            "C++",
            "JavaScript",
            "SQL",
            "HTML/CSS",
            "Custom"
        ]
    )

    if language == "Custom":
        language = st.text_input("Enter Programming Language")

    code = st.text_area(
        "Paste Your Code",
        height=300,
        placeholder="Paste your code here..."
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Review Code", use_container_width=True):

        if code.strip() == "":
            st.warning("Please paste your code.")
            return

        prompt = f"""
You are an experienced Senior Software Engineer.

Review the following {language} code.

Code:
{code}

Generate the response in the following format.

## Overall Review
Give a short summary of the code quality.

## Strengths
List 3 strengths.

## Issues Found
List bugs, bad practices, or code smells.

## Performance Suggestions
Suggest optimization opportunities.

## Best Practices
Provide 3 coding best practices.

## Improved Code
Provide a cleaner and improved version of the code.

Keep the response concise and well-formatted.
"""

        with st.spinner("Reviewing Code..."):

            response = ask_model(model, prompt)

        st.session_state.code_review = response

    # ---------------- Display ---------------- #

    if "code_review" in st.session_state:

        st.success("✅ Code Reviewed Successfully!")

        st.markdown("## Code Review")

        st.markdown(st.session_state.code_review)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.code_review,
                    "code_review"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.code_review,
                    "code_review"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")