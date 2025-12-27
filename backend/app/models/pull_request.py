from pydantic import BaseModel,Field
from typing import Optional

class PullRequest(BaseModel):
    number:int=Field(...,description="Pull request number")
    title:str=Field(...,description="Title of the pull request")
    body:Optional[str]=Field(None,description="detail description of the pull request")
    state:str=Field(...,description="State of the pull request e.g. open, closed, merged")
    created_at:str=Field(...,description="Creation date of the pull request")
    updated_at:Optional[str]=Field(None,description="Last update date of the pull request")
    merged:bool=Field(...,description="Indicates if the pull request has been merged")
    author:str=Field(...,description="Author of the pull request")

