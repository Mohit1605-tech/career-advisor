import os

# Only use Gemini if we have a valid environment API key
# The hardcoded key is leaked and won't work
USE_API = False  # Set to True only if you have a valid API key

try:
    from google import genai
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key and api_key != "AIzaSyCPXqsO3jO0TJqcWns6Q6bBhL7J4el9TB8":
        client = genai.Client(api_key=api_key)
        USE_API = True
    else:
        client = None
except Exception as e:
    print(f"Warning: Gemini not available: {e}")
    client = None

# Fallback career advice database
career_advice = {
    "doctor": "As a doctor, focus on: 1) Continue medical education & certifications 2) Build patient care expertise 3) Stay updated on healthcare tech 4) Consider specialization in high-demand fields",
    "engineer": "As an engineer, develop: 1) System design skills 2) Cloud platform expertise (AWS/GCP) 3) Problem-solving through projects 4) Leadership for senior roles",
    "designer": "As a designer, strengthen: 1) UI/UX principles 2) Design tools (Figma/Adobe) 3) User research skills 4) Portfolio with real case studies",
    "data scientist": "As a data scientist, master: 1) Machine learning algorithms 2) SQL & big data tools 3) A/B testing & statistics 4) Communication skills",
    "developer": "As a developer, improve: 1) System design & architecture 2) Advanced language concepts 3) DevOps & deployment 4) Open source contributions",
    "teacher": "As a teacher, focus on: 1) Latest pedagogical methods 2) Technology integration in classrooms 3) Student engagement techniques 4) Professional development",
    "lawyer": "As a lawyer, build: 1) Specialization in high-demand areas 2) Client management skills 3) Legal tech proficiency 4) Network in your practice area"
}

def get_fallback_response(prompt):
    """Return intelligent fallback advice based on career keywords."""
    prompt_lower = prompt.lower()
    
    for role, advice in career_advice.items():
        if role in prompt_lower:
            return advice
    
    # Generic fallback
    return """Career Growth Tips:
1. Build real-world projects in your domain
2. Network with professionals in your field
3. Get relevant certifications & upskill
4. Apply to positions consistently
5. Share knowledge through blogs/speaking"""

def ask_ai(prompt):
    global client, USE_API
    
    # Log to file for debugging
    with open("ask_ai_calls.log", "a") as f:
        f.write(f"ask_ai called with: {prompt}\n")
        f.write(f"USE_API={USE_API}, client={client}\n")
    
    if USE_API and client:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            print("API SUCCESS")
            return response.text
        except Exception as e:
            print(f"API Error: {e}, using fallback")
            return get_fallback_response(prompt)
    
    # Use fallback mode
    print("Using fallback mode (no valid API key)")
    fallback_response = get_fallback_response(prompt)
    with open("ask_ai_calls.log", "a") as f:
        f.write(f"Returning fallback: {fallback_response[:100]}...\n\n")
    return fallback_response