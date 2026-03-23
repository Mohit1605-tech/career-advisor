from resume_analyzer import analyze_resume
from skill_analyzer import analyze_skills
from recommender import recommend

resume_text = "Experienced in Python, SQL, Git, REST API, JavaScript, Machine Learning"
role = "ml enginner"

res = analyze_resume(resume_text, role)
print("--- AI OUTPUT ---")
print(res)
print("--- PARSED ---")
parsed = analyze_skills(res)
print(parsed)
