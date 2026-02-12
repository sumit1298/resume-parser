from fastapi import FastAPI
from backend.models.report import ResumeReport
from backend.database.db import engine, Base
from backend.routes.auth import router as auth_router
from backend.routes.admin import router as admin_router
from backend.routes.resume import router as resume_router
# from backend.routes.linkedin import router as linkedin_router

# Create DB tables (safe if already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resume Analyzer API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(resume_router, prefix="/resume", tags=["Resume"])
# app.include_router(linkedin_router, prefix="/linkedin", tags=["LinkedIn"])


@app.get("/")
def home():
    return {"message": "Resume API Running"}
