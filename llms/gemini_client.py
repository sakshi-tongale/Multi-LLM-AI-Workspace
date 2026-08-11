# import os
# from dotenv import load_dotenv
# from google import genai

# # Load environment variables
# load_dotenv()

# # Read Gemini API Key
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # Create Gemini client
# client = genai.Client(api_key=GEMINI_API_KEY)


# def ask_gemini(prompt):
#     response = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=prompt
#     )

#     return response.text
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text