from menus.core_menu import core_menu
from menus.developer_menu import developer_menu
from menus.data_science_menu import data_science_menu
from menus.advanced_menu import advanced_menu

print("=" * 50)
print("        Multi-LLM AI Workspace")
print("=" * 50)

while True:

    print("\n" + "=" * 50)
    print("Choose AI Model")
    print("=" * 50)
    print("1. Gemini")
    print("2. Claude")
    print("0. Exit")

    model = input("\nEnter your choice: ")

    if model == "0":
        print("\nThank you for using Multi-LLM AI Workspace!")
        break

    elif model not in ["1", "2"]:
        print("\nInvalid Choice!")
        continue

    print("\nMain Menu")
    print("1. Core AI Tools")
    print("2. Developer AI Tools")
    print("3. Data Science AI Tools")
    print("4. Advanced LLM Features")
    print("0. Exit")

    menu = input("\nEnter your choice: ")

    if menu == "1":
        core_menu(model)

    elif menu == "2":
        developer_menu(model)
    

    elif menu == "3":
        data_science_menu(model)

    elif menu == "4":
        advanced_menu(model)

    elif menu == "0":
        break

    else:
        print("\nInvalid Choice!")