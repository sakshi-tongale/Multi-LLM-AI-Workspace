# Stores conversation history for Claude

claude_history = []


def add_message(role, content):
    """
    Add a message to Claude's conversation history.
    """

    claude_history.append({
        "role": role,
        "content": content
    })


def get_history():
    """
    Return the full conversation history.
    """

    return claude_history


def clear_history():
    """
    Clear Claude's conversation history.
    """

    claude_history.clear()