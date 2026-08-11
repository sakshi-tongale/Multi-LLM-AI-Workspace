from llms.router import ask_model


def research_assistant(model):

    print("\n" + "=" * 50)
    print("AI Research Assistant")
    print("=" * 50)

    topic = input("\nEnter Research Topic: ")

    level = input("Research Level (Beginner/Intermediate/Advanced): ")

    prompt = f"""
You are an expert AI Research Assistant.

Research Topic:
{topic}

Research Level:
{level}

Generate a professional research report using the following format.

# Research Report

## Overview
(Brief introduction to the topic.)

## Key Concepts
(Explain the important concepts.)

## Applications
(List real-world applications.)

## Advantages
(Provide bullet points.)

## Challenges
(Provide bullet points.)

## Future Scope
(Explain future trends.)

## Conclusion
(Summarize the topic.)

Keep the report well-structured, concise, and easy to understand.
"""

    print("\nGenerating Research Report...\n")

    response = ask_model(model, prompt)

    print("\n" + "=" * 50)
    print("✅ Research Report Generated!")
    print("=" * 50)

    print(response)

    input("\nPress Enter to return...")