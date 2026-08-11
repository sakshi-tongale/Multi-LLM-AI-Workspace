import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def email_generator_page(model):

    st.title("📧 AI Email Generator")

    email_type = st.selectbox(
        "Select Email Type",
        [
            "Job Application",
            "HR Email",
            "Interview Follow-up",
            "Thank You Email",
            "Leave Application",
            "Meeting Request",
            "Custom Email"
        ]
    )

    recipient = st.text_input("Recipient Name")

    company = st.text_input("Company Name")

    subject = st.text_input("Email Subject")

    details = st.text_area(
        "Describe what you want to write",
        height=180
    )

    # ---------------- Generate Email ---------------- #

    if st.button("🚀 Generate Email", use_container_width=True):

        if details.strip() == "":
            st.warning("Please enter email details.")
            return

        prompt = f"""
Write a professional {email_type}.

Recipient: {recipient}
Company: {company}
Subject: {subject}

Details:
{details}

Generate:

- Subject
- Greeting
- Professional Email
- Closing
"""

        with st.spinner("Generating Email..."):

            response = ask_model(model, prompt)

        # Save response in session state
        st.session_state.email_response = response

    # ---------------- Show Generated Email ---------------- #

    if "email_response" in st.session_state:

        st.success("✅ Email Generated Successfully!")

        st.markdown("## Generated Email")

        st.markdown(st.session_state.email_response)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.email_response,
                    "email"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.email_response,
                    "email"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")