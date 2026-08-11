from tools.advanced.rag_pipeline import prepare_pdf, ask_pdf


def chat_with_pdf(model=None):
    """
    Chat with PDF Feature
    """

    pdf_path = input("\nEnter PDF path: ")

    index, chunks = prepare_pdf(pdf_path)

    print("\n✅ PDF Loaded Successfully!")

    while True:

        question = input("\nAsk a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            print("\nReturning to Advanced Menu...")
            break

        print("\nGenerating Answer...\n")

        answer = ask_pdf(question, index, chunks)

        print("=" * 60)
        print("Answer")
        print("=" * 60)
        print(answer)