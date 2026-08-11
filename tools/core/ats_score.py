from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model


def ats_score(model):
    print("\n===== ATS Score Analyzer =====")

    pdf_path = input("Enter the path of your resume PDF: ")

    try:
        resume_text = extract_text_from_pdf(pdf_path)

    except Exception as e:
        print(f"\nError reading PDF: {e}")
        return

    prompt = f"""
You are an expert ATS (Applicant Tracking System) Resume Reviewer.

Analyze the following resume.

Evaluate it based on:

1. Contact Information
2. Professional Summary
3. Skills
4. Work Experience
5. Projects
6. Education
7. Keywords & Technologies

Return the result in exactly this format:

ATS Score: XX/100

Section Scores:
- Contact Information:
- Professional Summary:
- Skills:
- Work Experience:
- Projects:
- Education:
- Keywords:

Strengths:
- ...

Weaknesses:
- ...

Missing Keywords:
- ...

Suggestions:
- ...

Resume:

{resume_text}
"""

    print("\nCalculating ATS Score...\n")

    response = ask_model(model, prompt)

    print("=" * 60)
    print("ATS SCORE REPORT")
    print("=" * 60)
    print(response)