import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Application
    APP_NAME = "AI Career Advisor API"
    APP_VERSION = "2.2.0"
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    
    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODELS = ["gemini-1.5-flash", "gemini-1.5-pro"]
    
    # Limits
    MAX_RESUME_LENGTH = 10000
    MIN_INPUT_LENGTH = 3
    REQUEST_TIMEOUT = 30
    
    # CORS
    ALLOWED_ORIGINS = ["*"]
    
    @classmethod
    def validate(cls):
        if not cls.GEMINI_API_KEY:
            raise ValueError("Missing GEMINI_API_KEY in environment variables")
