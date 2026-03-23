import re

# Skill patterns for resume matching
SKILL_PATTERNS = {
    "Python": r"\bpython\b",
    "Java": r"\bjava\b",
    "JavaScript": r"\b(javascript|js)\b",
    "SQL": r"\bsql\b",
    "AWS": r"\b(aws|amazon|ec2|s3)\b",
    "Cloud": r"\b(cloud|gcp|azure)\b",
    "Docker": r"\bdocker\b",
    "React": r"\breact\b",
    "Node.js": r"\bnode\.?js\b",
    "Statistics": r"\b(statistics|stats|statstics)\b",
    "Machine Learning": r"\b(machine learning|ml|ai|neural|deep learning)\b",
    "Data Engineering": r"\b(data engineering|etl|pipeline)\b",
    "DevOps": r"\bdevops\b",
    "Git": r"\bgit\b",
    "REST API": r"\b(rest|api|endpoint)\b"
}

# Required skills for each role
ROLE_REQUIRED = {
    "Data Scientist": ["Python", "SQL", "Machine Learning", "Statistics"],
    "Software Engineer": ["Python", "JavaScript", "Java", "Git", "REST API"],
    "DevOps Engineer": ["Docker", "Cloud", "Git", "DevOps", "SQL"],
    "Frontend Developer": ["JavaScript", "React", "Git", "REST API"],
    "Backend Developer": ["Python", "Java", "SQL", "REST API", "Database"],
    "Full Stack Developer": ["JavaScript", "React", "Node.js", "SQL", "Git"]
}

def analyze_resume(resume, role):
    """Analyze resume using pattern matching (no API dependency)."""
    found_skills = []
    missing_skills = []
    
    resume_lower = resume.lower()
    
    # Find skills in resume
    for skill, pattern in SKILL_PATTERNS.items():
        if re.search(pattern, resume_lower):
            found_skills.append(skill)
    
    # Determine required skills based on role
    required = ROLE_REQUIRED.get(role, ["Python", "SQL", "Git", "REST API"])
    
    # Find missing skills
    for req_skill in required:
        if req_skill not in found_skills:
            missing_skills.append(req_skill)
    
    # Calculate score
    if required:
        score = int((len(found_skills) / len(required)) * 100)
    else:
        score = 0
    
    # Format output
    output = f"""Skills:
- {chr(10).join('- ' + s for s in found_skills) if found_skills else 'None detected'}

Missing Skills:
- {chr(10).join('- ' + s for s in missing_skills) if missing_skills else 'All core skills present!'}

Resume Score: {score}

Suggestions:
- Add {max(1, len(missing_skills))} certifications or projects in missing skills
- Build a portfolio project using {found_skills[0] if found_skills else 'your top skill'}
- Practice coding interview problems on missing skills
"""
    
    return output