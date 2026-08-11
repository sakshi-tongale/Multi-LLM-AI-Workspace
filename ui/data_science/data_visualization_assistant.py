import streamlit as st
import pandas as pd

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def data_visualization_assistant_page(model):

    st.title("📊 AI Data Visualization Assistant")

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

    numerical = list(df.select_dtypes(include="number").columns)
    categorical = list(df.select_dtypes(exclude="number").columns)

    st.divider()

    st.subheader("Dataset Information")

    st.write("### Numerical Columns")
    st.write(numerical)

    st.write("### Categorical Columns")
    st.write(categorical)

    # ---------------- Generate ---------------- #

    if st.button("🚀 Generate Visualization Suggestions", use_container_width=True):

        prompt = f"""
You are an expert Data Visualization specialist.

Dataset Information:

Rows: {df.shape[0]}
Columns: {df.shape[1]}

Numerical Columns:
{numerical}

Categorical Columns:
{categorical}

Suggest the best visualizations for this dataset.

Generate the response in the following format.

## Recommended Charts

For each chart provide:

- Chart Name
- Columns to Use
- Why this chart is useful

Include charts such as:

- Bar Chart
- Line Chart
- Histogram
- Box Plot
- Scatter Plot
- Pie Chart
- Correlation Heatmap (if applicable)

Finally provide:

## Visualization Tips

Keep the response concise and professional.
"""

        with st.spinner("Generating Visualization Suggestions..."):

            response = ask_model(model, prompt)

        st.session_state.visualization_result = response

    # ---------------- Display ---------------- #

    if "visualization_result" in st.session_state:

        st.success("✅ Visualization Suggestions Generated!")

        st.markdown("## AI Visualization Report")

        st.markdown(st.session_state.visualization_result)

        st.divider()

        st.subheader("Export Report")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.visualization_result,
                    "visualization_report"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.visualization_result,
                    "visualization_report"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")