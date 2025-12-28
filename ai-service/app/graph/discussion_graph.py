from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from app.chains.discussion_chain import (
    create_discussion_chain,
    format_messages_for_analysis,
    parse_analysis_response
)


class GraphState(TypedDict):
    """State for the discussion analysis graph"""
    messages: List[Dict]
    formatted_discussion: str
    raw_analysis: str
    analysis: Dict


def format_node(state: GraphState) -> GraphState:
    """Node to format messages for analysis"""
    messages = state["messages"]
    formatted = format_messages_for_analysis(messages)
    
    return {
        **state,
        "formatted_discussion": formatted
    }


def analyze_node(state: GraphState) -> GraphState:
    """Node to analyze the discussion using LangChain"""
    chain = create_discussion_chain()
    
    discussion = state["formatted_discussion"]
    response = chain.invoke({"discussion": discussion})
    
    # Extract text from response
    raw_analysis = response.content if hasattr(response, 'content') else str(response)
    
    return {
        **state,
        "raw_analysis": raw_analysis
    }


def parse_node(state: GraphState) -> GraphState:
    """Node to parse the analysis into structured format"""
    raw_analysis = state["raw_analysis"]
    parsed = parse_analysis_response(raw_analysis)
    
    return {
        **state,
        "analysis": parsed
    }


def create_discussion_graph():
    """Create LangGraph workflow for discussion analysis"""
    
    # Create graph
    workflow = StateGraph(GraphState)
    
    # Add nodes
    workflow.add_node("format", format_node)
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("parse", parse_node)
    
    # Add edges
    workflow.set_entry_point("format")
    workflow.add_edge("format", "analyze")
    workflow.add_edge("analyze", "parse")
    workflow.add_edge("parse", END)
    
    # Compile graph
    app = workflow.compile()
    
    return app
