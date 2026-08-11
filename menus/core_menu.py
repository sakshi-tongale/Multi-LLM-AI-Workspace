from tools.core.general_chat import general_chat
from tools.core.resume_analyzer import resume_analyzer
from tools.core.ats_score import ats_score
from tools.core.cover_letter_generator import cover_letter_generator
from tools.core.email_generator import email_generator
from tools.core.meeting_notes_generator import meeting_notes_generator


def core_menu(model):

    while True:

        print("\n" + "=" * 50)
        print("Core AI Tools")
        print("=" * 50)

        print("1. General Chat")
        print("2. Resume Analyzer")
        print("3. ATS Score")
        print("4. Cover Letter Generator")
        print("5. Email Generator")
        print("6. Meeting Notes Generator")
        print("0. Back")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            general_chat(model)

        elif choice == "2":
            resume_analyzer(model)

        elif choice == "3":
            ats_score(model)

        elif choice == "4":
            cover_letter_generator(model)

        elif choice == "5":
            email_generator(model)

        elif choice == "6":
            meeting_notes_generator(model)


        elif choice == "0":
            break

        else:
            print("Invalid Choice!")