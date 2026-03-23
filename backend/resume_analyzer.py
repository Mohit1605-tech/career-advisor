from google import genai

client = genai.Client(api_key="AIzaSyAlef1aoirtHst-3D4AkkQFg5kycL99S3w")

def analyze_resume(resume, role):
    try:
        prompt = f"""
        Act as an expert career advisor.

        Resume:
        {resume}

        Target Role: {role}

        Give output in this format:

        Skills:
        - ...

        Missing Skills:
        - ...

        Resume Score: (out of 100)

        Suggestions:
        - ...
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return "Error analyzing resume. Try again later."