from llms.router import ask_model


def code_reviewer(model):

    print("\n" + "=" * 50)
    print("AI Code Reviewer")
    print("=" * 50)

    print("\nSelect Programming Language")
    print("=" * 50)

    print("1. Python")
    print("2. Java")
    print("3. C++")
    print("4. JavaScript")
    print("5. SQL")
    print("6. HTML/CSS")
    print("7. Custom")
    print("0. Back")

    choice = input("\nEnter your choice: ")

    languages = {
        "1": "Python",
        "2": "Java",
        "3": "C++",
        "4": "JavaScript",
        "5": "SQL",
        "6": "HTML/CSS"
    }

    if choice == "0":
        return

    elif choice == "7":
        language = input("\nEnter Programming Language: ")

    elif choice in languages:
        language = languages[choice]

    else:
        print("\n❌ Invalid Choice!")
        return

    print("\nPaste your code below.")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    prompt = f"""
You are an experienced Senior Software Engineer.

Review the following {language} code.

Code:
{code}

Generate the response in the following format.

## Overall Review
Give a short summary of the code quality.

## Strengths
List 3 strengths.

## Issues Found
List bugs, bad practices, or code smells.

## Performance Suggestions
Suggest optimization opportunities.

## Best Practices
Provide 3 coding best practices.

## Improved Code
Provide a cleaner and improved version of the code.

Keep the response concise and well-formatted.
"""

    print("\nReviewing Code...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("Code Review")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Developer Menu...")