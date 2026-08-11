import pandas as pd
from llms.router import ask_model


def eda_report_generator(model):

    print("\n" + "=" * 50)
    print("EDA Report Generator")
    print("=" * 50)

    csv_path = input("\nEnter CSV file path: ")

    try:
        df = pd.read_csv(csv_path)

    except Exception as e:
        print(f"\n❌ Error:\n{e}")
        input("\nPress Enter...")
        return

    rows, cols = df.shape

    missing = df.isnull().sum()

    duplicates = df.duplicated().sum()

    numerical = list(df.select_dtypes(include="number").columns)

    categorical = list(df.select_dtypes(exclude="number").columns)

    statistics = df.describe(include="all").to_string()

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

Generate:

## Dataset Overview

## Data Quality Assessment

## Key Insights

## Potential Problems

## Recommendations

Keep the report concise and professional.
"""

    print("\nGenerating EDA Report...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ EDA Report Generated Successfully!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return...")