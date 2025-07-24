import logging
from typing import List, Dict, Optional
from fastapi import HTTPException
from .gemini_model import GeminiModel
from .openrouter_model import OpenRouterModel
from backend.config import Config

logger = logging.getLogger(__name__)

class MultiModel:
    def __init__(self):
        self.models = []
        self._initialize_models()
    
    def _initialize_models(self):
        """Initialize all available AI models with fallback"""
        # Try to initialize Gemini models first
        if Config.GEMINI_API_KEY:
            for model_name in Config.GEMINI_MODELS:
                try:
                    gemini = GeminiModel(model_name)
                    self.models.append({
                        "name": f"Gemini: {model_name}",
                        "instance": gemini,
                        "priority": 1
                    })
                    logger.info(f"Added Gemini model: {model_name}")
                except Exception as e:
                    logger.warning(f"Failed to initialize Gemini {model_name}: {str(e)}")
        
        # Initialize OpenRouter models
        if Config.OPENROUTER_API_KEY:
            for model_id, model_name in Config.OPENROUTER_MODELS.items():
                try:
                    openrouter = OpenRouterModel(model_id)
                    self.models.append({
                        "name": f"OpenRouter: {model_name}",
                        "instance": openrouter,
                        "priority": 2
                    })
                    logger.info(f"Added OpenRouter model: {model_name}")
                except Exception as e:
                    logger.warning(f"Failed to initialize OpenRouter {model_name}: {str(e)}")
        
        # Sort models by priority (lower priority first)
        self.models.sort(key=lambda x: x["priority"])
        
        if not self.models:
            logger.error("No working AI models found")
            raise HTTPException(
                status_code=500,
                detail="AI service configuration failed"
            )
    
    async def generate_advice(self, skills: str, interests: str, resume_text: str = "") -> dict:
        """Generate career advice using available models with fallback"""
        prompt = self._build_prompt(skills, interests, resume_text)
        errors = []
        
        for model in self.models:
            try:
                logger.info(f"Trying model: {model['name']}")
                response = await model['instance'].generate_advice(prompt)
                return {
                    "success": True,
                    "advice": response,
                    "model": model['name']
                }
            except Exception as e:
                logger.warning(f"Model {model['name']} failed: {str(e)}")
                errors.append(f"{model['name']}: {str(e)}")
        
        # All models failed
        logger.error("All AI models failed to generate advice")
        raise HTTPException(
            status_code=500,
            detail=f"All models failed: {'; '.join(errors)}"
        )
    
    def _build_prompt(self, skills: str, interests: str, resume_text: str) -> str:
        """Build the standardized prompt for all models"""
        return f"""Analyze this career profile:
        Skills: {skills}
        Interests: {interests}
        Resume: {resume_text}
        
        Provide detailed career advice with valid URLs. Include:
        - Career path suggestions
        - Skills to develop
        - Job search strategies
        - Salary expectations
        - Industry trends
        - Learning resources"""
