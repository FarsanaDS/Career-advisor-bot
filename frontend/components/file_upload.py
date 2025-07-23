import io  # Add this import at the top of the file
from typing import Dict
import streamlit as st
from frontend.utils.resume_parser import ResumeParser
from backend.config import Config  # Make sure this is imported for MAX_RESUME_LENGTH


class FileUploadComponent:
    def __init__(self):
        self.parser = ResumeParser()
    
    def render(self) -> Dict:
        """Render file upload component and return resume data"""
        uploaded_file = st.file_uploader(
            "📄 Upload Resume (PDF)", 
            type=["pdf"],
            help="For more accurate suggestions"
        )
        
        resume_data = {"text": "", "thumbnail": None, "was_truncated": False}
        
        if uploaded_file:
            parsed_data = self.parser.parse(uploaded_file)
            if parsed_data:
                resume_data = parsed_data
                st.success(f"Processed {len(parsed_data['text']):,} characters "
                          f"({parsed_data['pages']} pages)")
                
                if parsed_data['was_truncated']:
                    st.warning(
                        f"Note: Only first ~{Config.MAX_RESUME_LENGTH//1000}KB will be analyzed "
                        f"(from {len(parsed_data['text'])//1000}KB total)"
                    )
                
                with st.expander("Preview"):
                    img_byte_arr = io.BytesIO()
                    parsed_data["thumbnail"].save(img_byte_arr, format='PNG')
                    st.image(img_byte_arr.getvalue(), width=200, caption="First Page Preview")
                    st.text_area("Extracted Text", 
                               value=parsed_data["display_text"], 
                               height=150,
                               label_visibility="collapsed")
        
        return resume_data