def load_css():
    return """
    <style>
        .stTextInput input, .stTextArea textarea {
            border: 1px solid #4b6cb7 !important;
            border-radius: 10px !important;
            padding: 10px !important;
        }
        .stButton button {
            background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
            color: white !important;
            border: none;
            border-radius: 10px;
            padding: 10px 24px;
        }
        .skill-chip {
            background: #4b6cb7;
            color: white;
            padding: 5px 12px;
            border-radius: 15px;
            margin: 5px;
            display: inline-block;
            font-size: 14px;
        }
        .error-box {
            background-color: #ffebee;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
        }
    </style>
    """