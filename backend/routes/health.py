from fastapi import APIRouter
from backend.config import Config
from backend.models.multi_model import MultiModel
import logging
from fastapi.responses import RedirectResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

# Initialize limiter and router
limiter = Limiter(key_func=get_remote_address)
router = APIRouter()
router.state.limiter = limiter
router.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

logger = logging.getLogger(__name__)

@router.get("/")
async def root():
    """Redirect root to health endpoint"""
    return RedirectResponse(url="/health")

@router.get("/health")
@limiter.limit("10/minute")
async def health_check():
    """Comprehensive health check endpoint with model status"""
    try:
        # Test configuration
        if not Config.GEMINI_API_KEY and not Config.OPENROUTER_API_KEY:
            raise RuntimeError("No API keys configured")
        
        # Try model initialization
        try:
            model_service = MultiModel()
            
            # Get detailed model status
            gemini_working = any("Gemini" in model['name'] for model in model_service.models)
            openrouter_working = any("OpenRouter" in model['name'] for model in model_service.models)
            
            model_status = "Model initialization successful"
        except Exception as e:
            model_status = f"Model initialization failed: {str(e)}"
            logger.error(model_status)
            gemini_working = False
            openrouter_working = False
        
        return {
            "status": "healthy",
            "app": Config.APP_NAME,
            "version": Config.APP_VERSION,
            "models": {
                "gemini": gemini_working,
                "openrouter": openrouter_working
            },
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
            "models": {
                "gemini": False,
                "openrouter": False
            },
            "model_status": "Initialization failed"
        }
