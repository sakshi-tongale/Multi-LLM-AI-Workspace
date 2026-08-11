import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def code_explainer_page(model):

    st.title("📖 AI Code Explainer")

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

    if st.button("🚀 Explain Code", use_container_width=True):

        if code.strip() == "":
            st.warning("Please paste your code.")
            return

        prompt = f"""
You are an expert {language} developer.

Analyze the following code.

Language:
{language}

Code:
{code}

Generate the response in the following format.

## Code Summary
Explain in 2–3 lines what the code does.

## Line-by-Line Explanation
Explain the important parts using bullet points.

## Best Practices
Give 3 improvement suggestions.

## Time Complexity
Mention only if applicable.

Keep the response concise and easy to understand.
"""

        with st.spinner("Analyzing Code..."):

            response = ask_model(model, prompt)

        st.session_state.code_explanation = response

    # ---------------- Display ---------------- #

    if "code_explanation" in st.session_state:

        st.success("✅ Code Explained Successfully!")

        st.markdown("## Code Explanation")

        st.markdown(st.session_state.code_explanation)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.code_explanation,
                    "code_explanation"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.code_explanation,
                    "code_explanation"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")