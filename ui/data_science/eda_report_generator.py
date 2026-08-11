import streamlit as st
import pandas as pd

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def eda_report_generator_page(model):

    st.title("📊 AI EDA Report Generator")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is None:
        return

    # ---------------- Load CSV ---------------- #

    try:
        df = pd.read_csv(uploaded_file)

    except Exception as e:
        st.error(f"Error reading CSV:\n{e}")
        return

    st.success("✅ CSV Loaded Successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ---------------- Dataset Statistics ---------------- #

    rows, cols = df.shape

    missing = df.isnull().sum()

    duplicates = df.duplicated().sum()

    numerical = list(df.select_dtypes(include="number").columns)

    categorical = list(df.select_dtypes(exclude="number").columns)

    statistics = df.describe(include="all").to_string()

    st.divider()

    st.subheader("Dataset Summary")

    st.write(f"**Numerical Columns:** {numerical}")

    st.write(f"**Categorical Columns:** {categorical}")

    st.write(f"**Duplicate Rows:** {duplicates}")

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate EDA Report", use_container_width=True):

        prompt = f"""
You are an expert Data Scientist.

Analyze the following dataset.

Dataset Overview

Rows: {rows}

Columns: {cols}

Missing Values

{missing.to_string()}

Duplicate Rows

{duplicates}

Numerical Columns

{numerical}

Categorical Columns

{categorical}

Summary Statistics

{statistics}

Generate the report in the following format.

## Dataset Overview

## Data Quality Assessment

## Key Insights

## Potential Problems

## Recommendations

Keep the report concise, professional, and well formatted.
"""

        with st.spinner("Generating EDA Report..."):

            response = ask_model(model, prompt)

        st.session_state.eda_report = response

    # ---------------- Display ---------------- #

    if "eda_report" in st.session_state:

        st.success("✅ EDA Report Generated Successfully!")

        st.markdown("## EDA Report")

        st.markdown(st.session_state.eda_report)

        st.divider()

        st.subheader("Export Report")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.eda_report,
                    "eda_report"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.eda_report,
                    "eda_report"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")