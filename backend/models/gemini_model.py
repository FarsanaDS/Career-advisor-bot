import google.generativeai as genai
import logging
from fastapi import HTTPException
from backend.config import Config

logger = logging.getLogger(__name__)

class GeminiModel:
    def __init__(self, model_name: str):
        self.model = None
        self.model_name = model_name
        self._initialize()
    
    def _initialize(self):
        """Initialize Gemini with comprehensive error handling"""
        try:
            # Verify API key first
            if not Config.GEMINI_API_KEY:
                raise ValueError("GEMINI_API_KEY is not configured")
            
            if not Config.GEMINI_API_KEY.startswith("AI"):
                logger.warning("GEMINI_API_KEY format appears invalid")
            
            genai.configure(api_key=Config.GEMINI_API_KEY)
            
            try:
                # Get available models to verify API key
                models = genai.list_models()
                if not any(model.name == self.model_name for model in models):
                    logger.warning(f"Model {self.model_name} not available")
                
                self.model = genai.GenerativeModel(self.model_name)
                logger.info(f"Gemini model initialized: {self.model_name}")
                return
            except Exception as e:
                logger.error(f"Failed to initialize {self.model_name}: {str(e)}")
                # Try the other model as fallback
                if self.model_name == "gemini-1.5-flash":
                    fallback = "gemini-1.5-pro"
                else:
                    fallback = "gemini-1.5-flash"
                
                try:
                    self.model = genai.GenerativeModel(fallback)
                    self.model_name = fallback
                    logger.info(f"Using fallback model: {fallback}")
                    return
                except Exception:
                    raise RuntimeError(f"Both {self.model_name} and fallback failed")
            
        except Exception as e:
            logger.exception(f"Gemini initialization failed for {self.model_name}")
            raise HTTPException(
                status_code=500,
                detail=f"Gemini AI service error: {str(e)}"
            )
    
    async def generate_advice(self, skills: str, interests: str, resume_text: str = "") -> str:
        """Generate career advice using Gemini"""
        try:
            prompt = f"""Analyze this career profile:
            Skills: {skills}
            Interests: {interests}
            Resume: {resume_text}
            
            Provide detailed career advice with valid URLs."""
            
            response = await self.model.generate_content_async(prompt)
            return response.text
        
        except Exception as e:
            logger.error(f"Error generating advice: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"Career advice generation failed: {str(e)}"
            )
