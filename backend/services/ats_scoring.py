def calculate_ats_score(resume_text: str):
    score = 0
    feedback = []

    lower_text = resume_text.lower()

    sections = ["education","skills","experience","projects"]

    for section in sections:
        if section in lower_text:
            score+= 10
        else:
            feedback.append(f"Missing section : {section}")
    
    keywords = [
        "python","sql","api","react",
        "machine learning","docker","fastapi"
    ]

    keyword_matches = 0

    for word in keywords:
        if word in lower_text:
            keyword_matches += 1

    score += keyword_matches * 5

    if keyword_matches < 3:
        feedback.append("Add more technical keywords")

    return {
        "score":min(score,100),
        "feedback":feedback
    }