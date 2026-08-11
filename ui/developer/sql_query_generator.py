import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def sql_query_generator_page(model):

    st.title("🗄️ AI SQL Query Generator")

    database = st.selectbox(
        "Select Database",
        [
            "MySQL",
            "PostgreSQL",
            "SQL Server",
            "SQLite",
            "Oracle",
            "MongoDB",
            "Custom"
        ]
    )

    if database == "Custom":
        database = st.text_input("Enter Database Name")

    user_request = st.text_area(
        "Describe the SQL query you need",
        height=200,
        placeholder="Example: Find the top 10 customers by total sales."
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate SQL Query", use_container_width=True):

        if user_request.strip() == "":
            st.warning("Please describe your SQL query requirement.")
            return

        prompt = f"""
You are an expert SQL developer.

Database Type:
{database}

User Request:
{user_request}

Generate:

1. SQL Query
2. Explanation of the query
3. Any assumptions made
4. Best practices (if applicable)

Format the response neatly.
"""

        with st.spinner("Generating SQL Query..."):

            response = ask_model(model, prompt)

        st.session_state.sql_query = response

    # ---------------- Display ---------------- #

    if "sql_query" in st.session_state:

        st.success("✅ SQL Query Generated Successfully!")

        st.markdown("## Generated SQL")

        st.markdown(st.session_state.sql_query)

        st.divider()

        st.subheader("Export")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.sql_query,
                    "sql_query"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.sql_query,
                    "sql_query"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")