from llms.router import ask_model


def python_code_generator(model):

    print("\n" + "=" * 50)
    print("AI Python Code Generator")
    print("=" * 50)

    print("\nSelect Code Type")
    print("=" * 50)

    print("1. Basic Python")
    print("2. Object-Oriented Programming (OOP)")
    print("3. Data Structures & Algorithms")
    print("4. File Handling")
    print("5. Web Development (Flask/FastAPI)")
    print("6. Data Analysis (Pandas)")
    print("7. Machine Learning")
    print("8. Automation Script")
    print("9. Custom")

    choice = input("\nEnter your choice: ")

    code_types = {
        "1": "Basic Python",
        "2": "Object-Oriented Programming",
        "3": "Data Structures & Algorithms",
        "4": "File Handling",
        "5": "Web Development",
        "6": "Data Analysis",
        "7": "Machine Learning",
        "8": "Automation Script",
        "9": "Custom"
    }

    if choice == "9":
        code_type = input("\nEnter Code Type: ")

    elif choice in code_types:
        code_type = code_types[choice]

    else:
        print("\n❌ Invalid Choice!")
        return

    print("\nDescribe what you want the Python program to do.")
    print("Example: Create a binary search algorithm.")

    task = input("\nYour Request: ")

    prompt = f"""
You are an expert Python developer.

Category:
{code_type}

Task:
{task}

Generate ONLY the following sections in this exact order.

## Python Code
- Provide clean, executable Python code.
- Keep comments minimal.

## Explanation
- Explain the solution in 4–5 bullet points only.

## Example
- Give one example input and output.

## Best Practices
- Give 3 bullet points only.

## Time Complexity
- Mention only the time complexity in one line.

Keep the entire response under 500 words.
Do not add introductions, conclusions, horizontal separators, or extra explanations.


"""

    print("\nGenerating Python Code...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ Python Code Generated Successfully!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Developer Menu...")