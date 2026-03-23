def recommend(skills, missing):
    
    suggestions = []

    if "Data Structures" in missing:
        suggestions.append("Practice DSA problems daily")

    if "Machine Learning" in missing:
        suggestions.append("Start learning ML basics")

    if len(skills) < 3:
        suggestions.append("Build more projects")

    suggestions.append("Apply to at least 5 internships per week")

    return suggestions

