import streamlit as st

from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def dataset_summary_generator_page(model):

    st.title("📄 AI Dataset Summary Generator")

    dataset_name = st.text_input("Dataset Name")

    description = st.text_area(
        "Describe the Dataset",
        height=200,
        placeholder="Example: Customer details including age, income, gender, purchases, and churn status."
    )

    if st.button("🚀 Generate Dataset Summary", use_container_width=True):

        if dataset_name.strip() == "" or description.strip() == "":
            st.warning("Please enter the dataset name and description.")
            return

        prompt = f"""
You are an expert Data Scientist.

Dataset Name:
{dataset_name}

Dataset Description:
{description}

Generate the response in the following format.

## Dataset Overview
Briefly explain the purpose of the dataset.

## Possible Features
List the likely input features.

## Target Variable
Mention the probable target variable.

## Suggested Machine Learning Task
(Classification, Regression, Clustering, etc.)

## Data Challenges
Mention possible issues such as:

- Missing values
- Duplicate data
- Outliers
- Class imbalance

## Recommendations

Provide 5 concise recommendations before model building.

Keep the response clear, concise, and well-formatted.
"""

        with st.spinner("Generating Dataset Summary..."):

            response = ask_model(model, prompt)

        st.session_state.dataset_summary = response

    # ---------------- Display Result ---------------- #

    if "dataset_summary" in st.session_state:

        st.success("✅ Dataset Summary Generated Successfully!")

        st.markdown("## Dataset Summary")

        st.markdown(st.session_state.dataset_summary)

        st.divider()

        st.subheader("Export Report")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("📄 Save as TXT", use_container_width=True):

                path = export_to_txt(
                    st.session_state.dataset_summary,
                    "dataset_summary"
                )

                st.success("✅ TXT file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")

        with col2:

            if st.button("📝 Save as DOCX", use_container_width=True):

                path = export_to_docx(
                    st.session_state.dataset_summary,
                    "dataset_summary"
                )

                st.success("✅ DOCX file saved successfully!")

                st.info(f"📁 Saved to:\n{path}")