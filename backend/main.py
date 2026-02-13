from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.models.report import ResumeReport
from backend.database.db import engine, Base
from backend.routes.auth import router as auth_router
from backend.routes.admin import router as admin_router
from backend.routes.resume import router as resume_router

# Create DB tables (safe if already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Resume Analyzer API")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])
app.include_router(resume_router, prefix="/resume", tags=["Resume"])


@app.get("/")
def home():
    return {"message": "Resume API Running"}
