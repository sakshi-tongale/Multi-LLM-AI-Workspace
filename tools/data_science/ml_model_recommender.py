import pandas as pd
from llms.router import ask_model


def ml_model_recommender(model):

    print("\n" + "=" * 50)
    print("ML Model Recommender")
    print("=" * 50)

    csv_path = input("\nEnter CSV file path: ")

    try:
        df = pd.read_csv(csv_path)

    except Exception as e:
        print(f"\n❌ Error:\n{e}")
        input("\nPress Enter...")
        return

    rows, cols = df.shape

    numerical = list(df.select_dtypes(include="number").columns)
    categorical = list(df.select_dtypes(exclude="number").columns)

    print("\nColumns in Dataset:")

    for column in df.columns:
        print(f"- {column}")

    target = input("\nEnter Target Column (or press Enter if unknown): ")

    prompt = f"""
You are an expert Machine Learning Engineer.

Dataset Information

Rows:
{rows}

Columns:
{cols}

Numerical Columns:
{numerical}

Categorical Columns:
{categorical}

Target Column:
{target if target else "Not Specified"}

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

    print("\nAnalyzing Dataset...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ ML Recommendation Generated!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return...")