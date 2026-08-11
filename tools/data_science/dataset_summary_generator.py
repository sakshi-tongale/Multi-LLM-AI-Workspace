from llms.router import ask_model


def dataset_summary_generator(model):

    print("\n" + "=" * 50)
    print("Dataset Summary Generator")
    print("=" * 50)

    dataset_name = input("\nDataset Name: ")

    print("\nDescribe the dataset.")
    print("Example: Customer details including age, income, gender, purchases, and churn status.")

    description = input("\nDescription: ")

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

    print("\nGenerating Dataset Summary...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ Dataset Summary Generated Successfully!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Data Science Menu...")