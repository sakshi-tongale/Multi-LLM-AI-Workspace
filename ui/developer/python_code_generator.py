import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def python_code_generator_page(model):

    st.title("💻 AI Python Code Generator")

    code_type = st.selectbox(
        "Select Code Type",
        [
            "Basic Python",
            "Object-Oriented Programming",
            "Data Structures & Algorithms",
            "File Handling",
            "Web Development",
            "Data Analysis",
            "Machine Learning",
            "Automation Script",
            "Custom"
        ]
    )

    if code_type == "Custom":
        code_type = st.text_input("Enter Custom Code Type")

    task = st.text_area(
        "Describe what you want the Python program to do",
        height=200,
        placeholder="Example: Create a binary search algorithm."
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate Python Code", use_container_width=True):

        if task.strip() == "":
            st.warning("Please describe your request.")
            return

        prompt = f"""
You are an expert Python developer.

Category:
{code_type}

Task:
{task}

Generate ONLY the following sections in this exact order.

## Python Code
- Provide clean, executable Python code.
- Keep comments minimal.

## Explanation
- Explain the solution in 4–5 bullet points only.

## Example
- Give one example input and output.

## Best Practices
- Give 3 bullet points only.

## Time Complexity
- Mention only the time complexity in one line.

Keep the entire response under 500 words.
Do not add introductions, conclusions, horizontal separators, or extra explanations.
"""

        with st.spinner("Generating Python Code..."):

            response = ask_model(model, prompt)

        st.session_state.python_code = response

    # ---------------- Display ---------------- #

    if "python_code" in st.session_state:

        st.success("✅ Python Code Generated Successfully!")

        st.markdown("## Generated Code")

        st.markdown(st.session_state.python_code)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.python_code,
                    "python_code"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.python_code,
                    "python_code"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")