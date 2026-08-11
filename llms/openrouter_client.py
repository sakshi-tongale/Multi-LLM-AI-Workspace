import os
from dotenv import load_dotenv
from openai import OpenAI

from llms.conversation_memory import (
    add_message,
    get_history
)

# Load environment variables
load_dotenv()

# Create OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def ask_openrouter(prompt):
    """
    Ask Claude with conversation memory.
    """

    # Save user's message
    add_message("user", prompt)

    # Get entire conversation history
    messages = get_history()

    # Send to Claude
    response = client.chat.completions.create(
        model="anthropic/claude-sonnet-5",
        messages=messages,
        temperature=0.7,
        max_tokens=2048
    )

    # Extract Claude's answer
    answer = response.choices[0].message.content

    # Save Claude's response
    add_message("assistant", answer)

    return answer