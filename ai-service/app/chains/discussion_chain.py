from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from typing import List, Dict


def create_discussion_chain():
    """Create a simple LangChain for discussion analysis"""
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are an AI assistant that analyzes chat discussions.
Your task is to provide a simple, clear analysis of the conversation.

Provide:
1. A brief summary (5-6 lines max)
2. Main topics discussed (3-5 topics)
3. Open questions raised (2-4 questions)
4. A short insight about the discussion

Keep your response structured and concise."""),
        ("user", """Analyze this discussion:

{discussion}

Provide your analysis in the following format:
SUMMARY: [your summary here]
TOPICS: [topic1, topic2, topic3]
QUESTIONS: [question1, question2]
INSIGHT: [your insight here]""")
    ])
    
    # Initialize LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3,
        max_tokens=500
    )
    
    # Create chain
    chain = prompt | llm
    
    return chain


def format_messages_for_analysis(messages: List[Dict]) -> str:
    """Format messages into a readable discussion format"""
    formatted = []
    for msg in messages:
        timestamp = msg.get('timestamp', '')
        username = msg.get('username', 'Unknown')
        content = msg.get('content', '')
        formatted.append(f"[{username}]: {content}")
    
    return "\n".join(formatted)


def parse_analysis_response(response_text: str) -> Dict:
    """Parse the LLM response into structured data"""
    lines = response_text.strip().split("\n")
    
    result = {
        "summary": "",
        "main_topics": [],
        "open_questions": [],
        "insight": ""
    }
    
    current_section = None
    
    for line in lines:
        line = line.strip()
        
        if line.startswith("SUMMARY:"):
            result["summary"] = line.replace("SUMMARY:", "").strip()
            current_section = "summary"
        elif line.startswith("TOPICS:"):
            topics_str = line.replace("TOPICS:", "").strip()
            result["main_topics"] = [t.strip() for t in topics_str.strip("[]").split(",")]
            current_section = "topics"
        elif line.startswith("QUESTIONS:"):
            questions_str = line.replace("QUESTIONS:", "").strip()
            result["open_questions"] = [q.strip() for q in questions_str.strip("[]").split(",")]
            current_section = "questions"
        elif line.startswith("INSIGHT:"):
            result["insight"] = line.replace("INSIGHT:", "").strip()
            current_section = "insight"
        elif current_section and line:
            # Continue previous section if multi-line
            if current_section == "summary":
                result["summary"] += " " + line
            elif current_section == "insight":
                result["insight"] += " " + line
    
    return result
