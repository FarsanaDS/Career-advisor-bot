from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.config import Config
from backend.utils.helpers import setup_logging
from backend.routes import career_advice, health

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
app.include_router(health.router)
app.include_router(career_advice.router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        log_level="info" if not Config.DEBUG else "debug"
    )