from fastapi import APIRouter, HTTPException
from typing import Dict
from backend.models.gemini_model import GeminiModel
from backend.utils.validators import validate_skills_interests, validate_resume_length

router = APIRouter()

@router.post("/career-advice")
async def get_career_advice(request: Dict):
    try:
        # Input validation
        skills = validate_skills_interests(request.get("skills"), "skills")
        interests = validate_skills_interests(request.get("interests"), "interests")
        resume_text = validate_resume_length(request.get("resume_text", ""))
        
        # Get AI response
        gemini = GeminiModel()
        advice = await gemini.generate_advice(skills, interests, resume_text)
        
        return {
            "success": True,
            "advice": advice,
            "model": gemini.model_name
        }

    except HTTPException:
        raise  # Re-raise HTTP exceptions
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )