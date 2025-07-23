from fastapi import APIRouter
from backend.config import Config
from backend.models.gemini_model import GeminiModel

router = APIRouter()

@router.get("/health")
async def health_check():
    """Endpoint for health checks"""
    return {
        "status": "healthy",
        "model": GeminiModel().model_name,
        "limits": {
            "max_resume_length": Config.MAX_RESUME_LENGTH,
            "min_input_length": Config.MIN_INPUT_LENGTH
        }
    }