from llms.openrouter_client import ask_openrouter

print("=" * 60)
print("Claude Chat (Conversation Memory)")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("\nGoodbye!")
        break

    print("\nClaude is thinking...\n")

    answer = ask_openrouter(question)

    print("=" * 60)
    print("Claude")
    print("=" * 60)
    print(answer)