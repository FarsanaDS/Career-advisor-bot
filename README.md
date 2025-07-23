# AI Career Advisor Pro 💼

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://career-advisor-frontend.onrender.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

AI Career Advisor Pro is an intelligent career guidance application that analyzes your skills, interests, and resume to provide personalized career recommendations. Powered by Google's Gemini AI, it offers actionable insights and resources to help you advance your career.

![AI Career Advisor Pro Screenshot](https://via.placeholder.com/800x400?text=Career+Advisor+Screenshot)

## Features ✨

- **Personalized Career Advice**: Get tailored recommendations based on your skills and interests
- **Resume Analysis**: Upload your resume for more accurate suggestions
- **AI-Powered Insights**: Leverages Google's Gemini AI for intelligent career guidance
- **Session History**: Track your previous queries and recommendations
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Tech Stack 🛠️

**Backend:**
- Python
- FastAPI
- Google Gemini API
- Uvicorn

**Frontend:**
- Streamlit
- PyMuPDF (for PDF processing)
- Pillow (image processing)

**Deployment:**
- Render.com
- Docker

## Live Demo 🌐

Experience the application live:  
[https://career-advisor-frontend.onrender.com](https://career-advisor-frontend.onrender.com)

## Local Development Setup 🛠️

### Prerequisites
- Python 3.11+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/career-advisor-bot.git
   cd career-advisor-bot
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # MacOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

### Running the Application

1. **Start the backend:**
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

2. **Start the frontend:**
   ```bash
   cd ../frontend
   streamlit run main.py
   ```

3. **Access the application:**
   - Backend: http://localhost:8000
   - Frontend: http://localhost:8501

## Deployment to Render 🚀

1. **Create a Render account** at [render.com](https://render.com/)
2. **Connect your GitHub repository**
3. **Create an Environment Group:**
   - Name: `gemini-api-key`
   - Add your Gemini API key
4. **Deploy the backend service:**
   - Select "Web Service"
   - Choose your repository
   - Name: `career-advisor-backend`
   - Runtime: Docker
   - Dockerfile Path: `Dockerfile`
   - Environment Variables:
     - `PORT`: 8000
     - `GEMINI_API_KEY`: from group `gemini-api-key`
5. **Deploy the frontend service:**
   - Wait for backend to deploy and note its URL
   - Create another "Web Service"
   - Name: `career-advisor-frontend`
   - Runtime: Docker
   - Dockerfile Path: `Dockerfile.frontend`
   - Environment Variables:
     - `PORT`: 8501
     - `BACKEND_URL`: URL of your backend service

## Project Structure 📁

```
career-advisor-bot/
├── backend/               # FastAPI backend
│   ├── main.py            # Application entry point
│   ├── config.py          # Configuration settings
│   ├── models/            # AI models
│   ├── routes/            # API endpoints
│   └── utils/             # Helper functions
├── frontend/              # Streamlit frontend
│   ├── main.py            # Frontend entry point
│   ├── components/        # UI components
│   ├── pages/             # Application pages
│   └── utils/             # Helper functions
├── Dockerfile             # Backend Docker configuration
├── Dockerfile.frontend    # Frontend Docker configuration
├── requirements.txt       # Python dependencies
└── .env.example           # Environment variables template
```

## Contact 📧

For questions or support, please contact:
- Farsana Thasnem PA - farsanathesni02@gmail.com
- Project Link: [https://github.com/FarsanaDS/Career-advisor-bot](https://github.com/FarsanaDS/Career-advisor-bot)

---

**Note**: This application provides AI-generated career advice. Always consult with professional career advisors before making important career decisions.
