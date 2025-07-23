import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import Config
from backend.utils.helpers import setup_logging
from backend.routes import career_advice
from backend.routes.health import router as health_router

# Initialize logging
setup_logging()

# Initialize and validate config
Config.validate()

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
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router)
app.include_router(career_advice.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Use PORT from environment
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info" if not Config.DEBUG else "debug"
    )
