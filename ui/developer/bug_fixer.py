import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def bug_fixer_page(model):

    st.title("🐞 AI Bug Fixer")

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
        "Paste Your Buggy Code",
        height=300,
        placeholder="Paste your code here..."
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Fix Bugs", use_container_width=True):

        if code.strip() == "":
            st.warning("Please paste your code.")
            return

        prompt = f"""
You are an expert software engineer.

Analyze and fix the following {language} code.

Code:
{code}

Generate the response in the following format.

## Bugs Found
List all bugs or issues.

## Why These Bugs Occur
Explain each issue briefly.

## Fixed Code
Provide the corrected code inside a Markdown code block.

## Improvements
List the improvements made.

## Prevention Tips
Provide 3 tips to avoid similar bugs.

Keep the response concise, clear, and well-formatted.
"""

        with st.spinner("Fixing Bugs..."):

            response = ask_model(model, prompt)

        st.session_state.bug_fix_result = response

    # ---------------- Display ---------------- #

    if "bug_fix_result" in st.session_state:

        st.success("✅ Bug Fix Generated Successfully!")

        st.markdown("## Bug Fix Result")

        st.markdown(st.session_state.bug_fix_result)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.bug_fix_result,
                    "bug_fix"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.bug_fix_result,
                    "bug_fix"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")