import pandas as pd
from llms.router import ask_model


def csv_data_analyzer(model):

    print("\n" + "=" * 50)
    print("CSV Data Analyzer")
    print("=" * 50)

    csv_path = input("\nEnter CSV file path: ")

    try:
        df = pd.read_csv(csv_path)

    except Exception as e:
        print(f"\n❌ Error reading CSV:\n{e}")
        input("\nPress Enter to return...")
        return

    print("\n✅ CSV Loaded Successfully!")
    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    while True:

        print("\n" + "=" * 50)
        print("Select Analysis")
        print("=" * 50)

        print("1. 📊 Dataset Overview")
        print("2. ❓ Missing Values")
        print("3. 📈 Basic Statistics")
        print("4. 💬 Ask Anything About Dataset")
        print("5. 📑 Full Dataset Report")
        print("0. ⬅ Back")

        choices = input(
            "\nEnter your choice(s) (Example: 1,2,3 or 5): "
        )

        selected = [item.strip() for item in choices.split(",")]

        if "0" in selected:
            break

        analysis = ""

        # -----------------------------------
        # Dataset Overview
        # -----------------------------------

        if "1" in selected:

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

        # -----------------------------------
        # Missing Values
        # -----------------------------------

        if "2" in selected:

            analysis += f"""
### Missing Values

{df.isnull().sum().to_string()}
"""

        # -----------------------------------
        # Basic Statistics
        # -----------------------------------

        if "3" in selected:

            analysis += f"""
### Basic Statistics

{df.describe(include='all').to_string()}
"""

        # -----------------------------------
        # Ask Anything
        # -----------------------------------

        if "4" in selected:

            question = input("\nAsk your question: ")

            analysis += f"""
### Dataset Columns

{list(df.columns)}

### Sample Data

{df.head(10).to_string()}

### User Question

{question}
"""

        # -----------------------------------
        # Full Dataset Report
        # -----------------------------------

        if "5" in selected:

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

        if analysis.strip() == "":
            print("\n❌ Please select a valid option.")
            continue

        # Convert selected options into readable names
        selected_names = []

        if "1" in selected:
            selected_names.append("Dataset Overview")

        if "2" in selected:
            selected_names.append("Missing Values")

        if "3" in selected:
            selected_names.append("Basic Statistics")

        if "4" in selected:
            selected_names.append("Question Answering")

        if "5" in selected:
            selected_names.append("Full Dataset Report")

        selected_text = ", ".join(selected_names)

        prompt = f"""
You are an expert Data Scientist.

The user requested the following analyses:

{selected_text}

Dataset Information:

{analysis}

IMPORTANT INSTRUCTIONS:

Generate ONLY the sections requested.

If Dataset Overview was requested, create:

## Dataset Overview

If Missing Values was requested, create:

## Missing Values Analysis

If Basic Statistics was requested, create:

## Basic Statistics Analysis

If Question Answering was requested, create:

## Answer to User Question

If Full Dataset Report was requested, create:

## Full Dataset Report

After the requested sections, always include:

## Key Insights

## Recommendations

Use bullet points where appropriate.

Keep the response professional, concise, and well-formatted.

Do NOT include sections that were not requested.
"""

        print("\nAnalyzing Dataset...\n")

        response = ask_model(model, prompt)

        print("\n" + "=" * 50)
        print("✅ Analysis Completed!")
        print("=" * 50)

        print(response)

        input("\nPress Enter to continue...")