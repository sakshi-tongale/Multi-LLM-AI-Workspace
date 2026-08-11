import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def research_assistant_page(model):

    st.title("📚 AI Research Assistant")

    topic = st.text_input("Research Topic")

    level = st.selectbox(
        "Research Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    if st.button("🚀 Generate Research Report", use_container_width=True):

        if topic.strip() == "":
            st.warning("Please enter a research topic.")
            st.stop()

        prompt = f"""
You are an expert AI Research Assistant.

Research Topic:
{topic}

Research Level:
{level}

Generate a professional research report using the following format.

# Research Report

## Overview

## Key Concepts

## Applications

## Advantages

## Challenges

## Future Scope

## Conclusion

Keep the report concise, professional, and well-structured.
"""

        with st.spinner("Generating Research Report..."):

            response = ask_model(model, prompt)

        st.session_state.research_report = response

    if "research_report" in st.session_state:

        st.success("✅ Research Report Generated!")

        st.markdown("## Research Report")

        st.markdown(st.session_state.research_report)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.research_report,
                    "research_report"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.research_report,
                    "research_report"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")