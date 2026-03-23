import os
from google import genai

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print("API SUCCESS")
        return response.text

    except Exception as e:
        print("ERROR:", e)   # 👈 IMPORTANT
        return str(e)