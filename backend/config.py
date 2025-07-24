import os
from dotenv import load_dotenv

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
        if not cls.GEMINI_API_KEY and not cls.OPENROUTER_API_KEY:
            raise ValueError("At least one AI API key must be provided")
