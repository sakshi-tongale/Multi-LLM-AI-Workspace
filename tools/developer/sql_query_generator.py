from llms.router import ask_model


def sql_query_generator(model):

    print("\n" + "=" * 50)
    print("AI SQL Query Generator")
    print("=" * 50)

    print("\n" + "=" * 50)
    print("Select Database")
    print("=" * 50)

    print("1. 🐬 MySQL")
    print("2. 🐘 PostgreSQL")
    print("3. 🏢 SQL Server")
    print("4. 📦 SQLite")
    print("5. 🔶 Oracle")
    print("6. 🍃 MongoDB")
    print("7. ✍️ Custom Database")
    print("0. ⬅ Back")

    choice = input("\nEnter your choice: ")

    database_options = {
        "1": "MySQL",
        "2": "PostgreSQL",
        "3": "SQL Server",
        "4": "SQLite",
        "5": "Oracle",
        "6": "MongoDB"
    }

    if choice == "0":
        return

    elif choice == "7":
        database = input("\nEnter Database Name: ")

    elif choice in database_options:
        database = database_options[choice]

    else:
        print("\n❌ Invalid Choice!")
        return

    print("\nDescribe what SQL query you need.")
    print("Example: Find the top 10 customers by total sales.")

    user_request = input("\nYour Request: ")

    prompt = f"""
You are an expert SQL developer.

Database Type:
{database}

User Request:
{user_request}

Generate:

1. SQL Query
2. Explanation of the query
3. Any assumptions made
4. Best practices (if applicable)

Format the response neatly.
"""

    print("\nGenerating SQL Query...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ SQL Query Generated Successfully!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Developer Menu...")