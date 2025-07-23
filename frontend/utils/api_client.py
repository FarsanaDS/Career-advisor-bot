import os
import requests
import streamlit as st
from typing import Dict, Optional
import asyncio
from backend.config import Config

class APIClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv("BACKEND_URL", "http://localhost:8000")
    async def get_advice_async(self, data: Dict) -> Optional[Dict]:
        """Async API call with retry"""
        for attempt in range(3):
            try:
                response = requests.post(
                    f"{self.base_url}/api/v1/career-advice",
                    json=data,
                    timeout=Config.REQUEST_TIMEOUT
                )
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == 2:
                    raise e
                await asyncio.sleep(1)
    
    def get_advice(self, data: Dict) -> Dict:
        """Get career advice with error handling"""
        try:
            response = requests.post(
                f"{self.base_url}/api/v1/career-advice",
                json=data,
                timeout=Config.REQUEST_TIMEOUT
            )
            
            response.raise_for_status()
            result = response.json()
            
            if not result.get("success"):
                raise ValueError(result.get("error", "Unknown API error"))
                
            return result
            
        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "advice": "⚠️ Our career service is currently unavailable.",
                "error": str(e)
            }
        except ValueError as e:
            return {
                "success": False,
                "advice": "⚠️ Could not process career advice.",
                "error": str(e)
            }