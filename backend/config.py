import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class Config:
    # Application
    APP_NAME = "AI Career Advisor Pro"
    APP_VERSION = "3.0.0"  # Bump version
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODELS = ["gemini-1.5-flash", "gemini-1.5-pro"]
    
    # OpenRouter
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    OPENROUTER_MODELS = {
        "mistralai/mixtral-8x7b-instruct": "Mixtral 8x7B Instruct",
        "google/gemma-7b-it": "Gemma 7B",
        "deepseek-ai/deepseek-coder-33b-instruct": "DeepSeek Coder 33B",
        "qwen/qwen-72b-chat": "Qwen 72B Chat",
    }
    
    # Limits
    MAX_RESUME_LENGTH = 10000
    MIN_INPUT_LENGTH = 3
    REQUEST_TIMEOUT = 30
    
    # CORS
    ALLOWED_ORIGINS = ["*"]
    
    @classmethod
    def validate(cls):
        """Validate configuration with detailed logging"""
        errors = []
        
        # Gemini validation
        if not cls.GEMINI_API_KEY:
            errors.append("Missing GEMINI_API_KEY in environment variables")
            logger.critical("GEMINI_API_KEY is not set")
        else:
            # Check if key is valid format
            if not cls.GEMINI_API_KEY.startswith("AI"):
                logger.warning("GEMINI_API_KEY doesn't start with 'AI' - may be invalid")
        
        # OpenRouter validation
        if not cls.OPENROUTER_API_KEY:
            errors.append("Missing OPENROUTER_API_KEY in environment variables")
            logger.critical("OPENROUTER_API_KEY is not set")
        else:
            if len(cls.OPENROUTER_API_KEY) < 30:
                logger.warning("OPENROUTER_API_KEY seems unusually short")
        
        if errors:
            raise ValueError("; ".join(errors))
