from typing import List, Dict, Any
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from app.chains.discussion_chain import (
    create_discussion_chain,
    format_messages_for_analysis,
    parse_analysis_response
)


class GraphState(BaseModel):
    messages: List[Dict[str, Any]] = Field(
        ...,
        min_items=1,
        description="List of discussion messages"
    )

    formatted_discussion: str = Field(
        default="",
        min_length=1,
        description="Formatted discussion text"
    )

    raw_analysis: str = Field(
        default="",
        min_length=1,
        description="Raw LLM analysis output"
    )

    analysis: Dict[str, Any] = Field(
        default_factory=dict,
        description="Parsed structured analysis"
    )


def format_node(state: GraphState) -> GraphState:
    formatted = format_messages_for_analysis(state.messages)

    return state.copy(update={
        "formatted_discussion": formatted
    })


def analyze_node(state: GraphState) -> GraphState:
    chain = create_discussion_chain()

    response = chain.invoke({
        "discussion": state.formatted_discussion
    })

    raw_analysis = response.content if hasattr(response, "content") else str(response)

    return state.copy(update={
        "raw_analysis": raw_analysis
    })


def parse_node(state: GraphState) -> GraphState:
    parsed = parse_analysis_response(state.raw_analysis)

    return state.copy(update={
        "analysis": parsed
    })


def create_discussion_graph():
    workflow = StateGraph(GraphState)

    #create nodes
    workflow.add_node("format", format_node)
    workflow.add_node("analyze", analyze_node)
    workflow.add_node("parse", parse_node)
    
    #set edges  between nodes
    workflow.set_entry_point("format")
    workflow.add_edge("format", "analyze")
    workflow.add_edge("analyze", "parse")
    workflow.add_edge("parse", END)

    graph=workflow.compile()
    return graph
