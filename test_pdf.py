from tools.advanced.rag_pipeline import prepare_pdf, ask_pdf

# Enter PDF
pdf_path = input("Enter PDF path: ")

# Prepare PDF
index, chunks = prepare_pdf(pdf_path)

print("\n✅ Vector Store Created Successfully!")

# Ask Questions
while True:

    question = input("\nAsk a question (type exit to quit): ")

    if question.lower() == "exit":
        print("\nThank you for using Chat with PDF!")
        break

    print("\nGenerating Answer...\n")

    answer = ask_pdf(question, index, chunks)

    print("=" * 60)
    print("Answer")
    print("=" * 60)
    print(answer)