import os
import requests
import streamlit as st
from typing import Dict, Optional
from backend.config import Config

class APIClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv("BACKEND_URL", "http://localhost:8000")
    
    def get_advice(self, data: Dict) -> Dict:
        """Get career advice with error handling"""
        try:
            response = requests.post(
                f"{self.base_url}/api/v1/career-advice",
                json=data,
                timeout=Config.REQUEST_TIMEOUT
            )
            
            # Handle non-200 responses
            if response.status_code != 200:
                return {
                    "success": False,
                    "advice": "⚠️ Service temporarily unavailable. Please try again later.",
                    "error": f"HTTP {response.status_code}"
                }
                
            result = response.json()
            
            if not result.get("success"):
                return {
                    "success": False,
                    "advice": "⚠️ Could not process career advice.",
                    "error": result.get("error", "Unknown API error")
                }
                
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
                "advice": "⚠️ Invalid response from service.",
                "error": str(e)
            }
