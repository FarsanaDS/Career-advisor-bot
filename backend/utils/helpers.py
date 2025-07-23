import re
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def fix_urls(text: str) -> str:
    """Ensure URLs are properly formatted in markdown"""
    # Convert plain URLs to markdown
    text = re.sub(r'(https?://\S+)', r'[Resource](\1)', text)
    # Fix malformed markdown links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', 
                 lambda m: f'[{m.group(1)}]({m.group(2).strip()})', 
                 text)
    return text

def sanitize_input(text: str) -> Optional[str]:
    """Sanitize user input"""
    if not text or not isinstance(text, str):
        return None
    return text.strip()

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )