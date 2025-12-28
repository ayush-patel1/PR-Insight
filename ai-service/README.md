# AI Service - Discussion Analysis

A Python-based AI service that analyzes chat discussions using LangChain and LangGraph.

## Features

- Summarizes discussions
- Identifies main topics
- Detects open questions
- Provides discussion insights

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` file:
```bash
cp .env.example .env
```

3. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_key_here
```

4. Run the service:
```bash
python app/main.py
```

The service will run on `http://localhost:8000`

## API Endpoints

### POST /analyze
Analyzes a discussion and returns insights.

**Request:**
```json
{
  "messages": [
    {
      "username": "john",
      "content": "What do you think about AI?",
      "timestamp": "2024-01-01T10:00:00Z"
    }
  ]
}
```

**Response:**
```json
{
  "summary": "Discussion about AI...",
  "main_topics": ["AI", "Technology"],
  "open_questions": ["What is the future of AI?"],
  "insight": "The discussion shows interest in AI development"
}
