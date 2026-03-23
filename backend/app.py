from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from ai_test import ask_ai
from recommender import recommend
from resume_analyzer import analyze_resume
from skill_analyzer import analyze_skills

app = Flask(__name__, static_folder='frontend', static_url_path='')
CORS(app)

@app.route("/test")
def test():
    return jsonify({"message": "API working successfully"})

# ✅ THIS IS THE IMPORTANT PART
@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.json

        prompt = data.get("prompt")

        if not prompt:
            return jsonify({"error": "No prompt provided"})

        print(f"DEBUG: Calling ask_ai with prompt: {prompt}")
        response = ask_ai(prompt)
        print(f"DEBUG: Response from ask_ai: {response}")

        return jsonify({"response": response})
    except Exception as e:
        print(f"DEBUG: ERROR in /ask: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"{type(e).__name__}: {str(e)}", "traceback": traceback.format_exc()})

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

@app.route("/")
def home():
    return send_from_directory('frontend', 'index.html')

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory('frontend', path)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)