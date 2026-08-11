import streamlit as st
import pandas as pd

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def csv_data_analyzer_page(model):

    st.title("📊 AI CSV Data Analyzer")

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

    st.divider()

    # ---------------- Analysis Options ---------------- #

    options = st.multiselect(
        "Select Analysis",
        [
            "Dataset Overview",
            "Missing Values",
            "Basic Statistics",
            "Ask Anything",
            "Full Dataset Report"
        ]
    )

    question = ""

    if "Ask Anything" in options:
        question = st.text_input(
            "Ask your question about the dataset"
        )

    # ---------------- Generate Analysis ---------------- #

    if st.button("🚀 Generate Analysis", use_container_width=True):

        if len(options) == 0:
            st.warning("Please select at least one analysis.")
            return

        analysis = ""

        # Dataset Overview
        if "Dataset Overview" in options:

            analysis += f"""
### Dataset Overview

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes}

First Five Rows:
{df.head().to_string()}
"""

        # Missing Values
        if "Missing Values" in options:

            analysis += f"""
### Missing Values

{df.isnull().sum().to_string()}
"""

        # Basic Statistics
        if "Basic Statistics" in options:

            analysis += f"""
### Basic Statistics

{df.describe(include='all').to_string()}
"""

        # Ask Anything
        if "Ask Anything" in options:

            analysis += f"""
### Dataset Columns

{list(df.columns)}

### Sample Data

{df.head(10).to_string()}

### User Question

{question}
"""

        # Full Dataset Report
        if "Full Dataset Report" in options:

            analysis += f"""
### Full Dataset Report

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Column Names:
{list(df.columns)}

Data Types:
{df.dtypes}

Missing Values:
{df.isnull().sum().to_string()}

Basic Statistics:
{df.describe(include='all').to_string()}

Sample Data:
{df.head().to_string()}
"""

        selected_text = ", ".join(options)

        prompt = f"""
You are an expert Data Scientist.

The user requested the following analyses:

{selected_text}

Dataset Information:

{analysis}

Generate ONLY the requested analyses.

If Dataset Overview was requested, generate:

## Dataset Overview

If Missing Values was requested, generate:

## Missing Values Analysis

If Basic Statistics was requested, generate:

## Basic Statistics Analysis

If Ask Anything was requested, generate:

## Answer to User Question

If Full Dataset Report was requested, generate:

## Full Dataset Report

After the requested sections always include:

## Key Insights

## Recommendations

Use bullet points where appropriate.

Keep the response professional and concise.
"""

        with st.spinner("Analyzing Dataset..."):

            response = ask_model(model, prompt)

        st.session_state.csv_analysis = response

    # ---------------- Display Result ---------------- #

    if "csv_analysis" in st.session_state:

        st.success("✅ Analysis Completed!")

        st.markdown("## Analysis Result")

        st.markdown(st.session_state.csv_analysis)

        st.divider()

        st.subheader("Export Report")

        col1, col2 = st.columns(2)

        # TXT Export
        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.csv_analysis,
                    "csv_analysis"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        # DOCX Export
        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.csv_analysis,
                    "csv_analysis"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")