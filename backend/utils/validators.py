from typing import Optional
from fastapi import HTTPException
from backend.config import Config

def validate_resume_length(text: str) -> str:
    """Ensure resume text is within limits"""
    if not text:
        return ""
    return text[:Config.MAX_RESUME_LENGTH]

def validate_skills_interests(text: str, field_name: str) -> str:
    """Validate skills/interests input"""
    if not text or len(text.strip()) < Config.MIN_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"{field_name} must be at least {Config.MIN_INPUT_LENGTH} characters"
        )
    return text.strip()