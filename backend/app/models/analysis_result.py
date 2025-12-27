from pydantic import BaseModel, Field
from typing import List, Optional 
from enum import Enum


class RiskLevel(str, Enum):
    low = "Low"
    medium = "Medium"
    high = "High"

class AnalysisResult(BaseModel):
    summary:str=Field(...,description="Summary of the analysis")
    checklist:Optional[List[str]]=Field(None,description="Checklist items generated from the analysis")
    recommendations:Optional[List[str]]=Field(None,description="Recommendations based on the analysis") 
    risk:RiskLevel=Field(...,description="Risk level associated with the analysis(Low,Medium,High)")
    issues_found:Optional[List[str]]=Field(None,description="List of issues found during the analysis")
    