from llms.router import ask_model


def summarize_chunk(model, chunk):
    """
    Summarize one chunk of a document.
    """

    prompt = f"""
You are an AI Document Summarizer.

Summarize the following document section.

Keep the summary concise.

Document Section:

{chunk}
"""

    return ask_model(model, prompt)