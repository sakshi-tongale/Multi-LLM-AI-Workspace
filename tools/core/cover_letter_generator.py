from utils.pdf_reader import extract_text_from_pdf
from llms.router import ask_model


def cover_letter_generator(model):
    print("\n===== AI Cover Letter Generator =====")

    # Resume
    pdf_path = input("Enter the path of your resume PDF: ")

    try:
        resume_text = extract_text_from_pdf(pdf_path) ## Reads the resume PDF.

    except Exception as e:
        print(f"\nError reading PDF: {e}")
        return

    # User Inputs
    job_title = input("Enter Job Title: ")
    company_name = input("Enter Company Name: ")

    print("\n(Optional)")
    job_description = input("Paste Job Description (or press Enter to skip): ")

    prompt = f"""
You are an expert career coach.

Using the resume below, write a professional cover letter.

Candidate Resume:
{resume_text}

Job Title:
{job_title}

Company:
{company_name}

Job Description:
{job_description}

Instructions:

- Keep it professional.
- Keep it to one page.
- Highlight relevant skills and projects.
- Mention enthusiasm for the company.
- End professionally.
"""

    print("\nGenerating Cover Letter...\n")

    response = ask_model(model, prompt)

    print("=" * 60)
    print("AI GENERATED COVER LETTER")
    print("=" * 60)
    print(response)