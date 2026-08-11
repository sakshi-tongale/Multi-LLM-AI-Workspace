import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def meeting_notes_generator_page(model):

    st.title("📝 AI Meeting Notes Generator")

    meeting_title = st.text_input("Meeting Title")

    participants = st.text_input(
        "Participants (comma separated)"
    )

    meeting_notes = st.text_area(
        "Paste Meeting Notes",
        height=250,
        placeholder="Paste your meeting notes here..."
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate Meeting Summary", use_container_width=True):

        if meeting_notes.strip() == "":
            st.warning("Please enter meeting notes.")
            return

        prompt = f"""
You are an AI Meeting Assistant.

Meeting Title:
{meeting_title}

Participants:
{participants}

Meeting Notes:
{meeting_notes}

Generate a professional meeting summary with the following sections:

1. Meeting Summary
2. Key Discussion Points
3. Decisions Made
4. Action Items
5. Next Steps

Format the response neatly.
"""

        with st.spinner("Generating Meeting Summary..."):

            response = ask_model(model, prompt)

        st.session_state.meeting_summary = response

    # ---------------- Display ---------------- #

    if "meeting_summary" in st.session_state:

        st.success("✅ Meeting Summary Generated Successfully!")

        st.markdown("## Meeting Summary")

        st.markdown(st.session_state.meeting_summary)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.meeting_summary,
                    "meeting_notes"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.meeting_summary,
                    "meeting_notes"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")