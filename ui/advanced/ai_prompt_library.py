import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def prompt_library_page(model):

    st.title("📖 AI Prompt Library")

    prompt_type = st.selectbox(
        "Select Prompt",
        [
            "Explain Code",
            "Summarize Text",
            "Translate Text",
            "Professional Email",
            "Interview Questions",
            "Brainstorm Ideas",
            "SQL Query Generator",
            "Resume Improvement"
        ]
    )

    user_input = st.text_area(
        "Enter your text",
        height=250
    )

    if st.button("🚀 Generate Response", use_container_width=True):

        if not user_input.strip():
            st.warning("Please enter some text.")
            st.stop()

        if prompt_type == "Explain Code":

            prompt = f"""
Explain the following code in simple language.

Code:
{user_input}
"""

        elif prompt_type == "Summarize Text":

            prompt = f"""
Summarize the following text in concise bullet points.

Text:
{user_input}
"""

        elif prompt_type == "Translate Text":

            prompt = f"""
Translate the following text into English.

Text:
{user_input}
"""

        elif prompt_type == "Professional Email":

            prompt = f"""
Write a professional email based on the following information.

Details:
{user_input}
"""

        elif prompt_type == "Interview Questions":

            prompt = f"""
Generate interview questions based on the following topic.

Topic:
{user_input}
"""

        elif prompt_type == "Brainstorm Ideas":

            prompt = f"""
Brainstorm creative ideas for the following topic.

Topic:
{user_input}
"""

        elif prompt_type == "SQL Query Generator":

            prompt = f"""
Generate an SQL query for the following requirement.

Requirement:
{user_input}
"""

        elif prompt_type == "Resume Improvement":

            prompt = f"""
Improve the following resume content professionally.

Resume:
{user_input}
"""

        with st.spinner("Generating Response..."):

            response = ask_model(model, prompt)

        st.session_state.prompt_library_response = response

    if "prompt_library_response" in st.session_state:

        st.success("✅ Response Generated!")

        st.markdown("## AI Response")

        st.markdown(st.session_state.prompt_library_response)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.prompt_library_response,
                    "prompt_library"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.prompt_library_response,
                    "prompt_library"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")