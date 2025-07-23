import fitz  # PyMuPDF
from PIL import Image
import io
import streamlit as st
from typing import Dict, Optional
try:
    from backend.config import Config
except ImportError:
    from ....backend.config import Config

class ResumeParser:
    def __init__(self, max_file_size: int = 5_000_000):
        self.max_file_size = max_file_size
    
    def parse(self, uploaded_file) -> Optional[Dict]:
        """Robust PDF parser with proper page access"""
        try:
            # Validate input
            if not uploaded_file.name.lower().endswith('.pdf'):
                st.error("Please upload a PDF file (.pdf extension)")
                return None
                
            if uploaded_file.size > self.max_file_size:
                st.error(f"File too large (max {self.max_file_size//1_000_000}MB)")
                return None
            
            # Process PDF
            file_bytes = uploaded_file.getvalue()
            
            with fitz.open(stream=file_bytes) as doc:
                # Document validation
                if doc.is_encrypted:
                    if not doc.authenticate(""):
                        st.error("Password-protected PDFs are not supported")
                        return None
                
                if doc.page_count == 0:
                    st.error("Empty PDF document")
                    return None
                
                # Extract text
                full_text = ""
                display_text = ""
                for i in range(min(20, len(doc))):  # Process up to 20 pages
                    page = doc.load_page(i)
                    page_text = page.get_text("text") + "\n\n"
                    full_text += page_text
                    
                    # Build display version
                    if len(display_text) < Config.MAX_RESUME_LENGTH:
                        remaining = Config.MAX_RESUME_LENGTH - len(display_text)
                        display_text += page_text[:remaining]
                    
                    # Early exit if we have enough content
                    if len(full_text) >= Config.MAX_RESUME_LENGTH * 1.2:
                        break
                
                # Finalize display text
                display_text = display_text[:Config.MAX_RESUME_LENGTH]
                if len(full_text) > Config.MAX_RESUME_LENGTH:
                    display_text += "..."
                
                # Generate thumbnail
                first_page = doc.load_page(0)
                pix = first_page.get_pixmap()
                img_bytes = pix.tobytes("png")
                thumbnail = Image.open(io.BytesIO(img_bytes))
                
                return {
                    "text": full_text[:Config.MAX_RESUME_LENGTH],
                    "display_text": display_text,
                    "thumbnail": thumbnail,
                    "pages": len(doc),
                    "was_truncated": len(full_text) > Config.MAX_RESUME_LENGTH,
                    "status": "success"
                }
                
        except fitz.FileDataError:
            st.error("Corrupted PDF file. Please try another file.")
            return None
        except fitz.EmptyFileError:
            st.error("Empty PDF file. Please upload a valid file.")
            return None
        except Exception as e:
            st.error(f"""
            ⚠️ PDF Processing Error:
            {str(e)}
            
            This usually means:
            1. The PDF has complex formatting
            2. It's a scanned document (image-based)
            3. The file is corrupted
            
            Try converting to a simpler PDF or upload a different file.
            """)
            return None
