from llms.router import ask_model


def prompt_library(model=None):

    while True:

        print("\n" + "=" * 50)
        print("Prompt Library")
        print("=" * 50)

        print("1. Explain Code")
        print("2. Summarize Text")
        print("3. Translate Text")
        print("4. Professional Email")
        print("5. Interview Questions")
        print("6. Brainstorm Ideas")
        print("7. SQL Query Generator")
        print("8. Resume Improvement")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("\nReturning to Advanced Menu...")
            break

        user_input = input("\nEnter your text:\n")

        if choice == "1":

            prompt = f"""
Explain the following code in simple language.

Code:
{user_input}
"""

        elif choice == "2":

            prompt = f"""
Summarize the following text in concise bullet points.

Text:
{user_input}
"""

        elif choice == "3":

            prompt = f"""
Translate the following text into English.

Text:
{user_input}
"""

        elif choice == "4":

            prompt = f"""
Write a professional email based on the following information.

Details:
{user_input}
"""

        elif choice == "5":

            prompt = f"""
Generate interview questions based on the following topic.

Topic:
{user_input}
"""

        elif choice == "6":

            prompt = f"""
Brainstorm creative ideas for the following topic.

Topic:
{user_input}
"""

        elif choice == "7":

            prompt = f"""
Generate an SQL query for the following requirement.

Requirement:
{user_input}
"""

        elif choice == "8":

            prompt = f"""
Improve the following resume content professionally.

Resume:
{user_input}
"""

        else:
            print("\nInvalid choice!")
            continue

        print("\nGenerating Response...\n")

        response = ask_model(model, prompt)

        print("=" * 60)
        print("AI Response")
        print("=" * 60)
        print(response)

        input("\nPress Enter to continue...")