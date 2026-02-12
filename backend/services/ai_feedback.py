def generate_ai_feedback(resume_text:str):
    suggestions = []

    if "project" not in resume_text.lower():
        suggestions.append("Add at least 3 projects descriptions.")

    if "experience" not in resume_text.lower():
        suggestions.append("Include work experience or Internships.")

    if "python" not in resume_text.lower():
        suggestions.append("Mention python projects or experiences.")

    if len(resume_text.split())<200:
        suggestions.append("Resume content is too short, Add more detail.")

    if not suggestions:
        suggestions.append("Resume looks strong. Minor improvements only.")

    return suggestions
