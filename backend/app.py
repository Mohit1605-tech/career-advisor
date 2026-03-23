from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_test import ask_ai
from recommender import recommend
from resume_analyzer import analyze_resume
from skill_analyzer import analyze_skills

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Career Advisor Backend Running 🚀"

@app.route("/test")
def test():
    return jsonify({"message": "API working successfully"})

# ✅ THIS IS THE IMPORTANT PART
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json

    prompt = data.get("prompt")

    if not prompt:
        return jsonify({"error": "No prompt provided"})

    response = ask_ai(prompt)

    return jsonify({"response": response})

@app.route("/analyze_resume", methods=["POST"])
def analyze():
    data = request.json

    resume = data.get("resume")
    role = data.get("role")

    if not resume or not role:
        return jsonify({"error": "Missing resume or role"})

    # Step 1: AI analysis
    result = analyze_resume(resume, role)

    # Step 2: Extract skills
    skill_data = analyze_skills(result)

    # Step 3: Get recommendations
    recommendations = recommend(skill_data["skills"], skill_data["missing"])

    # Step 4: Return response
    return jsonify({
        "analysis": result,
        "skills": skill_data["skills"],
        "missing_skills": skill_data["missing"],
        "recommendations": recommendations
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)