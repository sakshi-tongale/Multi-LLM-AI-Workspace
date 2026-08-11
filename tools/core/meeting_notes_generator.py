from llms.router import ask_model


def meeting_notes_generator(model):

    print("\n" + "=" * 50)
    print("AI Meeting Notes Generator")
    print("=" * 50)

    meeting_title = input("\nMeeting Title: ")
    participants = input("Participants: ")

    print("\nPaste your meeting notes below.")
    print("Press Enter after each line.")
    print("When finished, type END on a new line.\n")

    notes = []

    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        notes.append(line)

    meeting_notes = "\n".join(notes)

    prompt = f"""
You are an AI Meeting Assistant.

Meeting Title:
{meeting_title}

Participants:
{participants}

Meeting Notes:
{meeting_notes}

Generate a professional meeting summary with the following sections:

1. Meeting Summary
2. Key Discussion Points
3. Decisions Made
4. Action Items
5. Next Steps

Format the response neatly.
"""

    print("\nGenerating Meeting Summary...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("Meeting Summary")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return to the Core Menu...")