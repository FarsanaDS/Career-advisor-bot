import google.generativeai as genai
import logging
from fastapi import HTTPException
from backend.config import Config

logger = logging.getLogger(__name__)

class GeminiModel:
    def __init__(self):
        self.model = None
        self.model_name = None
        self._initialize()
    
    def _initialize(self):
        """Initialize Gemini with fallback handling"""
        try:
            genai.configure(api_key=Config.GEMINI_API_KEY)

            # Use the provided model name or default
            try:
                self.model = genai.GenerativeModel(self.model_name)
                logger.info(f"Using Gemini model: {self.model_name}")
                return
            except Exception as e:
                logger.warning(f"Failed to initialize {self.model_name}: {str(e)}")
                
            # Try preferred models in order
            for model_name in Config.GEMINI_MODELS:
                try:
                    self.model = genai.GenerativeModel(model_name)
                    self.model_name = model_name
                    logger.info(f"Using model: {model_name}")
                    return
                except Exception as e:
                    logger.warning(f"Failed to initialize {model_name}: {str(e)}")
                    continue
            
            raise RuntimeError("No working Gemini model found")
        
        except Exception as e:
            logger.error(f"Gemini initialization failed: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail="AI service configuration failed"
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
