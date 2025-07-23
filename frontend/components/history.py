import streamlit as st
from typing import List, Dict
from datetime import datetime

class HistoryComponent:
    def __init__(self):
        if "history" not in st.session_state:
            st.session_state.history = []
    
    def add_entry(self, skills: str, response: Dict):
        """Add new entry to history"""
        st.session_state.history.append({
            "time": datetime.now().strftime("%H:%M"),
            "skills": skills,
            "response": response["advice"],
            "model": response.get("model", "unknown")
        })
    
    def render(self):
        """Render history component"""
        with st.expander("📜 Session History"):
            for idx, item in enumerate(st.session_state.history[::-1]):
                st.markdown(f"**{idx+1}. {item['time']}** ({item['model']})")
                st.caption(f"Skills: {item['skills']}")
                st.markdown(item['response'][:200] + "...")