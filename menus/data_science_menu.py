from tools.data_science.dataset_summary_generator import dataset_summary_generator
from tools.data_science.csv_data_analyzer import csv_data_analyzer
from tools.data_science.eda_report_generator import eda_report_generator
from tools.data_science.data_visualization_assistant import data_visualization_assistant
from tools.data_science.ml_model_recommender import ml_model_recommender


def data_science_menu(model):

    while True:

        print("\n" + "=" * 50)
        print("Data Science AI Tools")
        print("=" * 50)

        print("1. Dataset Summary Generator")
        print("2. CSV Data Analyzer")
        print("3. EDA Report Generator")
        print("4. Data Visualization Assistant")
        print("5. ML Model Recommender")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            dataset_summary_generator(model)

        elif choice == "2":
            csv_data_analyzer(model)

        elif choice == "3":
            eda_report_generator(model)

        elif choice == "4":
            data_visualization_assistant(model)

        elif choice == "5":
            ml_model_recommender(model)

        elif choice == "0":
            break

        else:
            print("\n❌ Invalid Choice!")