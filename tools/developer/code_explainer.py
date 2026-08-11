from llms.router import ask_model


def code_explainer(model):

    print("\n" + "=" * 50)
    print("AI Code Explainer")
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
You are an expert {language} developer.

Analyze the following code.

Language:
{language}

Code:
{code}

Generate the response in the following format.

## Code Summary
Explain in 2–3 lines what the code does.

## Line-by-Line Explanation
Explain the important parts using bullet points.

## Best Practices
Give 3 improvement suggestions.

## Time Complexity
Mention only if applicable.

Keep the response concise and easy to understand.
"""

    print("\nAnalyzing Code...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("Code Explanation")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Developer Menu...")