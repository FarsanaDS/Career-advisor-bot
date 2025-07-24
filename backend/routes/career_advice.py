from fastapi import APIRouter, HTTPException
from typing import Dict
from backend.models.multi_model import MultiModel
from backend.utils.validators import validate_skills_interests, validate_resume_length
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/career-advice")
async def get_career_advice(request: Dict):
    try:
        # Input validation
        skills = validate_skills_interests(request.get("skills"), "skills")
        interests = validate_skills_interests(request.get("interests"), "interests")
        resume_text = validate_resume_length(request.get("resume_text", ""))
        
        # Get AI response
        model_service = MultiModel()
        result = await model_service.generate_advice(skills, interests, resume_text)
        
        return {
            "success": True,
            "advice": result["advice"],
            "model": result["model"]
        }

    except HTTPException as he:
        logger.error(f"HTTPException in career advice: {he.detail}")
        raise he
    except Exception as e:
        logger.exception("Unexpected error in career advice endpoint")
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
