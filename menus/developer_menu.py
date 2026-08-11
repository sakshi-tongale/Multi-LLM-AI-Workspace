from tools.developer.sql_query_generator import sql_query_generator
from tools.developer.python_code_generator import python_code_generator
from tools.developer.code_explainer import code_explainer
from tools.developer.code_reviewer import code_reviewer
from tools.developer.bug_fixer import bug_fixer


def developer_menu(model):

    while True:

        print("\n" + "=" * 50)
        print("Developer AI Tools")
        print("=" * 50)

        print("1. SQL Query Generator")
        print("2. Python Code Generator")
        print("3. Code Explainer")
        print("4. Code Reviewer")
        print("5. Bug Fixer")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            sql_query_generator(model)

        elif choice == "2":
            python_code_generator(model)

        elif choice == "3":
            code_explainer(model)
            

        elif choice == "4":
            code_reviewer(model)

        elif choice == "5":
            bug_fixer(model)

        elif choice == "0":
            break

        else:
            print("\n❌ Invalid Choice!")