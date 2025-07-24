import requests
import json
import logging
from fastapi import HTTPException
from backend.config import Config

logger = logging.getLogger(__name__)

class OpenRouterModel:
    def __init__(self, model_id: str):
        self.model_id = model_id
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
    
    async def generate_advice(self, prompt: str) -> str:
        """Generate career advice using OpenRouter API"""
        try:
            headers = {
                "Authorization": f"Bearer {Config.OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": self.model_id,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,
                "max_tokens": 1500
            }
            
            response = requests.post(
                self.api_url,
                headers=headers,
                data=json.dumps(data),
                timeout=30
            )
            
            response.raise_for_status()
            result = response.json()
            
            return result['choices'][0]['message']['content']
        
        except Exception as e:
            logger.error(f"OpenRouter error: {str(e)}")
            raise HTTPException(
                status_code=500,
                detail=f"OpenRouter request failed: {str(e)}"
            )
