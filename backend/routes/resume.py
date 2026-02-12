from fastapi import APIRouter, UploadFile, File, Depends
from backend.utils.security import get_current_user
from backend.services.resume_parser import parse_resume
from backend.services.ats_scoring import calculate_ats_score
from backend.services.ai_feedback import generate_ai_feedback
from sqlalchemy.orm import Session
from backend.database.db import get_db
from backend.models.report import ResumeReport
router = APIRouter()

@router.post("/upload")
async def upload_resume(
    file:UploadFile = File(...),
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    text = await parse_resume(file)

    ats_result = calculate_ats_score(text)
    ai_feedback = generate_ai_feedback(text)

    report = ResumeReport(
        user_email = user["email"],
        filename = file.filename,
        ats_score = ats_result["score"],
        feedback=";".join(ai_feedback)
    )

    db.add(report)
    db.commit()

    return {
        "filename":file.filename,
        "resume_text":text[:500],
        "ats_score":ats_result["score"],
        "ats_feedback":ats_result["feedback"],
        "ai_feedback":ai_feedback
    }


@router.get("/history")
def get_resume_history(
    user = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    reports = db.query(ResumeReport).filter(
        ResumeReport.user_email == user["email"]
    ).all()

    return reports