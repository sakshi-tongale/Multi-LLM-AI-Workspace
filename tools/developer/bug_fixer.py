from llms.router import ask_model


def bug_fixer(model):

    print("\n" + "=" * 50)
    print("AI Bug Fixer")
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

    print("\nPaste your buggy code below.")
    print("Type END on a new line when finished.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)

    prompt = f"""
You are an expert software engineer.

Analyze and fix the following {language} code.

Code:
{code}

Generate the response in the following format.

## Bugs Found
List all bugs or issues.

## Why These Bugs Occur
Explain each issue briefly.

## Fixed Code
Provide the corrected code inside a Markdown code block.

## Improvements
List the improvements made.

## Prevention Tips
Provide 3 tips to avoid similar bugs.

Keep the response concise, clear, and well-formatted.
"""

    print("\nFixing Bugs...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("Bug Fix Result")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Developer Menu...")