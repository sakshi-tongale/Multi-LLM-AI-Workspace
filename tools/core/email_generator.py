from llms.router import ask_model
from utils.file_exporter import export_to_txt, export_to_docx


def email_generator(model):

    print(">>> NEW EMAIL GENERATOR LOADED <<<")

    print("\n" + "=" * 50)
    print("AI Email Generator")
    print("=" * 50)

    print("\nSelect Email Type")
    print("1. Job Application")
    print("2. HR Email")
    print("3. Interview Follow-up")
    print("4. Thank You Email")
    print("5. Leave Application")
    print("6. Meeting Request")
    print("7. Custom Email")

    choice = input("\nEnter your choice: ")

    email_types = {
        "1": "Job Application",
        "2": "HR Email",
        "3": "Interview Follow-up",
        "4": "Thank You Email",
        "5": "Leave Application",
        "6": "Meeting Request",
        "7": "Custom Email"
    }

    email_type = email_types.get(choice, "Custom Email")

    recipient = input("Recipient Name: ")
    company = input("Company Name: ")
    subject = input("Email Subject: ")

    print("\nDescribe what you want to write:")
    details = input()

    prompt = f"""
Write a professional {email_type}.

Recipient: {recipient}
Company: {company}
Subject: {subject}

Details:
{details}

Generate:
- Subject
- Greeting
- Professional email
- Closing
"""

    print("\nGenerating Email...\n")


    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("Generated Email")
    print("=" * 50)

    print(response)

    print("\n" + "=" * 50)
    print("Do you want to save this?")
    print("=" * 50)

    print("1. Save as TXT")
    print("2. Save as DOCX")
    print("3. Save as Both")
    print("0. Don't Save")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        txt_path = export_to_txt(response, "email")
        print(f"\n✅ TXT saved to:\n{txt_path}")

    elif choice == "2":
        docx_path = export_to_docx(response, "email")
        print(f"\n✅ DOCX saved to:\n{docx_path}")

    elif choice == "3":
        txt_path = export_to_txt(response, "email")
        docx_path = export_to_docx(response, "email")

        print("\n✅ Files saved successfully!")
        print(f"TXT : {txt_path}")
        print(f"DOCX: {docx_path}")

    else:
        print("\nFile was not saved.")

  
    