from tools.advanced.research_assistant import research_assistant
from tools.advanced.chat_with_pdf import chat_with_pdf
from tools.advanced.document_summarizer import document_summarizer
from tools.advanced.prompt_library import prompt_library
from tools.advanced.document_qa import document_qa


def advanced_menu(model):

    while True:

        print("\n" + "=" * 50)
        print("Advanced LLM Features")
        print("=" * 50)

        print("1. Research Assistant")
        print("2. Chat with PDF")
        print("3. Document Summarizer")
        print("4. Prompt Library")
        print("5. Document Q&A")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            research_assistant(model)

        elif choice == "2":
            chat_with_pdf(model)

        elif choice == "3":
            document_summarizer(model)

        elif choice == "4":
            prompt_library(model)

        elif choice == "5":
            document_qa(model)

        elif choice == "0":
            break

        else:
            print("\n❌ Invalid Choice!")