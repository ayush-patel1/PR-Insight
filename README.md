# Real-Time AI Discussion & Analysis App

A full-stack MERN application with a Python AI service for real-time chat discussions and AI-powered analysis. This project demonstrates authentication, WebSocket communication, and AI integration.

## Features

- User authentication (register/login with JWT)
- Real-time chat using Socket.io
- AI-powered discussion analysis
- Clean, responsive UI
- Separate Python AI service using LangChain and LangGraph

## Tech Stack

### Backend (Node.js)
- Express.js
- MongoDB with Mongoose
- Socket.io for real-time communication
- JWT authentication
- bcrypt for password hashing

### Frontend (React)
- React 18
- React Router
- Socket.io-client
- Axios
- Context API for state management

### AI Service (Python)
- FastAPI
- LangChain
- LangGraph
- OpenAI API
- Pydantic for data validation

## Project Structure

```
├── backend/           # Node.js Express backend
├── frontend/          # React frontend
├── ai-service/        # Python AI service
└── README.md
```

## Setup Instructions

### Prerequisites

- Node.js (v16+)
- Python (v3.9+)
- MongoDB (local or Atlas)
- OpenAI API key

### 1. Backend Setup

```bash
cd backend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env and add your values:
# PORT=5000
# MONGODB_URI=mongodb://localhost:27017/discussion-app
# JWT_SECRET=your_secret_key
# FRONTEND_URL=http://localhost:3000
# AI_SERVICE_URL=http://localhost:8000

# Start the server
npm run dev
```

The backend will run on `http://localhost:5000`

### 2. AI Service Setup

```bash
cd ai-service

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Edit .env and add your OpenAI API key:
# OPENAI_API_KEY=your_openai_key
# PORT=8000

# Start the service
python app/main.py
```

The AI service will run on `http://localhost:8000`

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
cp .env.example .env

# Edit .env:
# REACT_APP_API_URL=http://localhost:5000

# Start the app
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

1. Open `http://localhost:3000` in your browser
2. Register a new account
3. Login with your credentials
4. Start chatting in the discussion room
5. Click "Analyze Discussion" to get AI insights

## API Endpoints

### Backend (Port 5000)

**Authentication**
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user

**Chat**
- `GET /api/chat/messages` - Get all messages
- `POST /api/chat/message` - Save a message

**Analysis**
- `POST /api/analysis/request` - Request AI analysis

### AI Service (Port 8000)

- `POST /analyze` - Analyze discussion messages
- `GET /health` - Health check

## AI Analysis Features

The AI service provides:
- **Summary**: Brief overview of the discussion (5-6 lines)
- **Main Topics**: Key topics discussed (3-5 topics)
- **Open Questions**: Questions raised during discussion (2-4)
- **Insight**: Overall discussion insight

## Development Notes

This is a fresher-level project designed for:
- College portfolios
- Internship applications
- Learning full-stack development
- Understanding real-time communication
- Exploring AI integration

The code is intentionally kept simple and readable, with some patterns that could be optimized in production but are perfect for learning.

## Known Limitations

- No message pagination (shows last 100 messages)
- Basic error handling
- Simple UI without advanced features
- AI analysis uses basic prompts (not advanced NLP)
- No user profiles or avatars
- No message editing or deletion

## Future Improvements

- Add message pagination
- Implement typing indicators
- Add user profiles
- Support multiple chat rooms
- Add message reactions
- Improve AI analysis with more sophisticated prompts
- Add message search functionality

## License

This project is open source and available for educational purposes.

## Author

Built as a college-level full-stack project demonstrating MERN stack with Python AI integration.
