from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model


def resume_analyzer(model):
    print("\n===== Resume Analyzer =====")

    pdf_path = input("Enter the path of your resume PDF: ")

    try:
        resume_text = extract_text_from_pdf(pdf_path)
    except Exception as e:
        print(f"\nError reading PDF: {e}")
        return

    prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume and provide:

1. ATS Score (out of 100)
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions for Improvement

Resume:

{resume_text}
"""

    print("\nAnalyzing resume...\n")

    response = ask_model(model, prompt)

    print("=" * 50)
    print("Resume Analysis")
    print("=" * 50)
    print(response)