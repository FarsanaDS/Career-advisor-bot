import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import Config
from backend.utils.helpers import setup_logging
from backend.routes import career_advice
from backend.routes.health import router as health_router

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize and validate config
try:
    Config.validate()
except Exception as e:
    logger.critical(f"Configuration validation failed: {str(e)}")
    raise RuntimeError(f"Configuration error: {str(e)}") from e

# Create FastAPI app
app = FastAPI(
    title=Config.APP_NAME,
    description="Backend for processing career advice requests",
    version=Config.APP_VERSION
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info("Application starting up...")
    try:
        # Warm up models
        from backend.models.multi_model import MultiModel
        model_service = MultiModel()
        logger.info("AI models initialized successfully")
    except Exception as e:
        logger.critical(f"Startup model initialization failed: {str(e)}")
        # Don't crash - we'll handle it in health check

# Include routers
app.include_router(health_router)
app.include_router(career_advice.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info" if not Config.DEBUG else "debug"
    )
