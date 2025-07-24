from fastapi import APIRouter
from backend.config import Config
from backend.models.multi_model import MultiModel

router = APIRouter()

@router.get("/health")
async def health_check():
    """Endpoint for health checks"""
    try:
        # Test model initialization without generating content
        MultiModel()
        return {
            "status": "healthy",
            "models_available": True,
            "limits": {
                "max_resume_length": Config.MAX_RESUME_LENGTH,
                "min_input_length": Config.MIN_INPUT_LENGTH
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "models_available": False
        }
