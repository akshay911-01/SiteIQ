from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class SiteCreate(BaseModel ):
    name: str = Field(min_length=1, max_length=100)
    location: str = Field(min_length=1, max_length=255)
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
class SiteResponse(BaseModel):
    model_config=ConfigDict(from_attributes=True)
    id:str
    name:str
    location:str
    latitude:float
    longitude:float
    created_at:datetime
