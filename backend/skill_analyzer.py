def analyze_skills(ai_output):
    skills = []
    missing = []

    lines = ai_output.split("\n")

    mode = None

    for line in lines:
        line = line.strip()

        if "Missing Skills:" in line:
            mode = "missing"
            continue

        if "Skills:" in line:
            mode = "skills"
            continue
            
        if "Suggestions:" in line or "Resume Score:" in line:
            mode = None
            continue

        if line.startswith("-"):
            if mode == "skills":
                skills.append(line.replace("-", "").strip())
            elif mode == "missing":
                missing.append(line.replace("-", "").strip())

    return {
        "skills": skills,
        "missing": missing
    }