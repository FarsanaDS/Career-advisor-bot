# AI Career Advisor Pro 🤖💼

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://career-advisor-frontend.onrender.com)
[![Multi-Model AI](https://img.shields.io/badge/Powered%20By-Gemini%20%2B%20OpenRouter-blue?style=for-the-badge)](https://openrouter.ai)

**An intelligent career guidance system** that uses multiple AI models to provide reliable career advice, even during peak usage times. Get personalized career path recommendations, skill development guidance, and industry insights powered by cutting-edge AI.

## Key Features ✨

- **Multi-Model AI Architecture**: Automatically switches between Gemini and OpenRouter models for reliable service
- **Resume Analysis**: Extract insights from uploaded resumes
- **Personalized Recommendations**: Career paths tailored to your skills and interests
- **Skill Gap Identification**: Discover skills to develop for career advancement
- **Model Transparency**: See which AI generated your advice
- **Session History**: Track your previous queries and recommendations

## Tech Stack 🛠️

**Backend:**
- Python
- FastAPI
- Gemini API + OpenRouter API
- Uvicorn

**Frontend:**
- Streamlit
- PyMuPDF (PDF processing)
- Pillow (image processing)

**Deployment:**
- Render.com
- Docker

## Live Demo 🌐

Experience the application now:  
[https://career-advisor-frontend.onrender.com](https://career-advisor-frontend.onrender.com)

## How It Works 🔍

1. **Input Your Profile**: Share your skills, interests, and optionally upload a resume
2. **AI Analysis**: Our system analyzes your profile using multiple AI models
3. **Smart Fallback**: Automatically switches models if one service is unavailable
4. **Personalized Advice**: Receive tailored career recommendations
5. **Model Attribution**: See which AI generated your advice

## Local Development Setup 🛠️

### Prerequisites
- Python 3.11+
- [Google Gemini API Key](https://aistudio.google.com/app/apikey)
- [OpenRouter API Key](https://openrouter.ai/keys)
- Git

### Installation

```bash
# Clone repository
git clone https://github.com/FarsanaDS/Career-advisor-bot.git
cd Career-advisor-bot

# Create virtual environment
python -m venv venv

# Activate environment
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Running the Application

1. **Start Backend:**
```bash
cd backend
uvicorn main:app --reload --port 8000
```

2. **Start Frontend (in new terminal):**
```bash
cd ../frontend
streamlit run main.py
```

3. **Access the Application:**
- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501
- API Documentation: http://localhost:8000/docs

## Deployment to Render 🚀

1. **Create a Render account** at [render.com](https://render.com/)
2. **Create Environment Group:**
   - Name: `ai-api-keys`
   - Add `GEMINI_API_KEY` and `OPENROUTER_API_KEY`
3. **Deploy Backend Service:**
   - Select "Web Service"
   - Connect your GitHub repository
   - Name: `career-advisor-backend`
   - Runtime: Docker
   - Dockerfile Path: `Dockerfile`
   - Environment Variables:
     - `PORT`: 8000
     - `GEMINI_API_KEY`: from group `ai-api-keys`
     - `OPENROUTER_API_KEY`: from group `ai-api-keys`
4. **Deploy Frontend Service:**
   - Note backend URL after deployment
   - Create another "Web Service"
   - Name: `career-advisor-frontend`
   - Runtime: Docker
   - Dockerfile Path: `Dockerfile.frontend`
   - Environment Variables:
     - `PORT`: 8501
     - `BACKEND_URL`: URL of backend service

## Project Structure 📁

```
career-advisor-bot/
├── backend/               # FastAPI backend
│   ├── main.py            # Application entry point
│   ├── config.py          # Configuration settings
│   ├── models/            # AI models (Gemini + OpenRouter)
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
├── .env.example           # Environment variables template
└── README.md              # Project documentation
```

## Supported AI Models 🤖

| Provider | Model | Specialization |
|----------|-------|----------------|
| **Google** | Gemini 1.5 Pro | Career path recommendations |
| **Google** | Gemini 1.5 Flash | Fast career insights |
| **Mistral AI** | Mixtral 8x7B Instruct | Structured career advice |
| **Google** | Gemma 7B | Educational guidance |
| **DeepSeek** | Coder 33B | Technical career paths |
| **Qwen** | Qwen 72B Chat | General career counseling |

## Contact 📧

For questions or support:
- Project Lead: Farsana Thasnem PA
- Email: farsanathesni02@gmail.com
- Project Repository: [https://github.com/FarsanaDS/Career-advisor-bot](https://github.com/FarsanaDS/Career-advisor-bot)

---

**Note**: This application provides AI-generated career advice. While we strive for accuracy, always consult with professional career advisors before making important career decisions. The AI models may occasionally produce unexpected results - use discretion when implementing suggestions.
