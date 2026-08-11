import streamlit as st
import pandas as pd

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def ml_model_recommender_page(model):

    st.title("🤖 AI ML Model Recommender")

    uploaded_file = st.file_uploader(
        "Upload CSV Dataset",
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

    st.success("✅ Dataset Loaded Successfully!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    st.divider()

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    # ---------------- Dataset Information ---------------- #

    numerical = list(df.select_dtypes(include="number").columns)
    categorical = list(df.select_dtypes(exclude="number").columns)

    st.divider()

    st.subheader("Dataset Information")

    st.write("### Numerical Columns")
    st.write(numerical)

    st.write("### Categorical Columns")
    st.write(categorical)

    target = st.selectbox(
        "Select Target Column (Optional)",
        ["Not Specified"] + list(df.columns)
    )

    # ---------------- Generate ---------------- #

    if st.button("🚀 Recommend ML Model", use_container_width=True):

        prompt = f"""
You are an expert Machine Learning Engineer.

Dataset Information

Rows:
{df.shape[0]}

Columns:
{df.shape[1]}

Numerical Columns:
{numerical}

Categorical Columns:
{categorical}

Target Column:
{target}

Recommend the best machine learning approach.

Generate the response using exactly this format.

## Problem Type
(Classification / Regression / Clustering / Recommendation / Time Series / Unknown)

## Recommended Models

For each model include:

- Model Name
- Why it is suitable

## Data Preprocessing

Mention:

- Missing values
- Encoding
- Feature scaling
- Feature selection

## Evaluation Metrics

Recommend suitable evaluation metrics.

## Next Steps

Give practical recommendations.

Do not assume information that is not present.

Keep the response concise and professional.
"""

        with st.spinner("Analyzing Dataset..."):

            response = ask_model(model, prompt)

        st.session_state.ml_recommendation = response

    # ---------------- Display ---------------- #

    if "ml_recommendation" in st.session_state:

        st.success("✅ ML Recommendation Generated Successfully!")

        st.markdown("## ML Recommendation Report")

        st.markdown(st.session_state.ml_recommendation)

        st.divider()

        st.subheader("Export Report")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.ml_recommendation,
                    "ml_model_recommendation"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.ml_recommendation,
                    "ml_model_recommendation"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")