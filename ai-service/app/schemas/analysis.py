from pydantic import BaseModel
from typing import List
from datetime import datetime


class Message(BaseModel):
    username: str
    content: str
    timestamp: datetime


class AnalysisRequest(BaseModel):
    messages: List[Message]


class AnalysisResponse(BaseModel):
    summary: str
    main_topics: List[str]
    open_questions: List[str]
    insight: str
