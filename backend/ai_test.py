import os
from google import genai

client = genai.Client(api_key="AIzaSyCPXqsO3jO0TJqcWns6Q6bBhL7J4el9TB8")

def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        print("API SUCCESS")
        return response.text

    except Exception as e:
        print("ERROR:", e)
        return f"Assistant: {str(e)}"