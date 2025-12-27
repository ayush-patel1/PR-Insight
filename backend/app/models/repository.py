from pydantic import BaseModel, Field
from typing import Optional

class Repository(BaseModel):
    name:str=Field(...,description="Name of Github repository")
    owner:str=Field(None,description="Owner of the repository")
    description:Optional[str]=Field(None,description="Description of the repository")
    private:bool=Field(...,description="Is the repository private or public")
    url:Optional[str]=Field(None,description="URL of the repository")
    created_at:Optional[str]=Field(None,description="Creation date of the repository")
    updated_at:Optional[str]=Field(None,description="Last update date of the repository")

