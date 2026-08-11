from llms.gemini_client import ask_gemini
from llms.openrouter_client import ask_openrouter


def ask_model(model, prompt):

    # ---------- Gemini ----------
    if model in ["1", "Gemini"]:
        return ask_gemini(prompt)

    # ---------- Claude ----------
    elif model in ["2", "Claude"]:

        try:
            return ask_openrouter(prompt)

        except Exception:

            print("\n⚠️ Claude is currently unavailable.")
            print("⚠️ Switching to Gemini...\n")

            return ask_gemini(prompt)

    return "Invalid Model Selected!"