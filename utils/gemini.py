from google import genai
from google.genai import types
from config import GEMINI_API,SYSTEM_PROMPT
client = genai.Client(api_key=GEMINI_API)

async def generate_response(user_message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.9
            ),contents=user_message
        )
        return response.text
    except Exception as e:
        print(e)
        return None