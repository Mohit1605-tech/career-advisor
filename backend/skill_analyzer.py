def analyze_skills(ai_output):
    skills = []
    missing = []

    lines = ai_output.split("\n")

    mode = None

    for line in lines:
        line = line.strip()

        if "Skills:" in line:
            mode = "skills"
            continue

        if "Missing Skills:" in line:
            mode = "missing"
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