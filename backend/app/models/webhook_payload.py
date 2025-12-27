from pydantic import BaseModel, Field   
from typing import Optional

from pull_request import PullRequest
from repository import Repository

class WebhookPayload(BaseModel):
    action: str = Field(..., description="Action performed on the pull request")
    pull_request: Optional[PullRequest] = Field(..., description="Details of the pull request only if present")
    repository: Repository = Field(..., description="Details of the repository")