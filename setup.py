from setuptools import setup, find_packages

setup(
    name="career_advisor_bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "fastapi", "uvicorn", "python-dotenv", "google-generativeai", "streamlit", "pymupdf", "Pillow", "requests", "python-multipart"
    ],
)
