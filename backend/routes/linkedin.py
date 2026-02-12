# from fastapi import APIRouter,Depends
# from pydantic import BaseModel
# from backend.utils.security import get_current_user
# from backend.services.linkedin_analyzer import analyze_linkedin
# from backend.models.linkedin import LinkedInRequest

# router = APIRouter()

# class LinkedInProfile(BaseModel):
#     profile_text:str


# @router.post("/analyze")
# def analyze_linkedin_route(data: LinkedInRequest):
#     return analyze_linkedin(data)
