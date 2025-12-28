from typing import List, Dict
from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.graph.discussion_graph import create_discussion_graph


class DiscussionAnalysisService:
    """Service for analyzing discussions"""
    
    def __init__(self):
        self.graph = create_discussion_graph()
    
    def analyze_discussion(self, request: AnalysisRequest) -> AnalysisResponse:
        """Analyze a discussion and return structured insights"""
        
        # Convert messages to dict format
        messages = [msg.model_dump() for msg in request.messages]
        
        # Run the graph
        initial_state = {
            "messages": messages,
            "formatted_discussion": "",
            "raw_analysis": "",
            "analysis": {}
        }
        
        result = self.graph.invoke(initial_state)
        
        # Extract analysis
        analysis = result["analysis"]
        
        # Create response
        response = AnalysisResponse(
            summary=analysis.get("summary", "No summary available"),
            main_topics=analysis.get("main_topics", []),
            open_questions=analysis.get("open_questions", []),
            insight=analysis.get("insight", "No insight available")
        )
        
        return response
