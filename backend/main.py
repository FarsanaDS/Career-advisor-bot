import os
import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from backend.config import Config
from backend.utils.helpers import setup_logging
from backend.routes import career_advice
from backend.routes.health import router as health_router

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

# Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

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

# Add rate limiter to app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health_router)
app.include_router(career_advice.router, prefix="/api/v1")

# Apply rate limiting to health endpoint
app.add_api_route(
    "/health",
    endpoint=limiter.limit("10/minute")(health_router.routes[1].endpoint),
    methods=["GET"],
    include_in_schema=True
)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        log_level="info" if not Config.DEBUG else "debug"
    )
