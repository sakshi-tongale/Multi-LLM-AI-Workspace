import pandas as pd
from llms.router import ask_model


def data_visualization_assistant(model):

    print("\n" + "=" * 50)
    print("Data Visualization Assistant")
    print("=" * 50)

    csv_path = input("\nEnter CSV file path: ")

    try:
        df = pd.read_csv(csv_path)

    except Exception as e:
        print(f"\n❌ Error reading CSV:\n{e}")
        input("\nPress Enter to return...")
        return

    numerical = list(df.select_dtypes(include="number").columns)
    categorical = list(df.select_dtypes(exclude="number").columns)

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

    print("\nGenerating Visualization Suggestions...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ Visualization Suggestions Generated!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return...")