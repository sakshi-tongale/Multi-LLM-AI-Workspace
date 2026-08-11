from llms.router import ask_model

def general_chat(model):
    print("\n===== General AI Chat =====")

    while True:
        prompt = input("\nYou: ")

        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        response = ask_model(model, prompt)

        print("\nAI:")
        print(response)