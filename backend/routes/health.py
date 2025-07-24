from fastapi import APIRouter
from backend.config import Config
from backend.models.multi_model import MultiModel
import logging
from fastapi.responses import RedirectResponse

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/")
async def root():
    """Redirect root to health endpoint"""
    return RedirectResponse(url="/health")

@router.get("/health")
async def health_check():
    """Comprehensive health check endpoint"""
    try:
        # Test configuration
        if not Config.GEMINI_API_KEY and not Config.OPENROUTER_API_KEY:
            raise RuntimeError("No API keys configured")
        
        # Test model initialization
        try:
            model_service = MultiModel()
            model_status = "Model initialization successful"
        except Exception as e:
            model_status = f"Model initialization failed: {str(e)}"
            logger.error(model_status)
            raise
        
        return {
            "status": "healthy",
            "app": Config.APP_NAME,
            "version": Config.APP_VERSION,
            "models_initialized": True,
            "model_status": model_status,
            "limits": {
                "max_resume_length": Config.MAX_RESUME_LENGTH,
                "min_input_length": Config.MIN_INPUT_LENGTH
            }
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "models_initialized": False
        }
