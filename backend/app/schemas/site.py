from datetime import datetime
from pydantic import BaseModel


class SiteCreate(BaseModel):
    name: str
    location: str
    latitude: float
    longitude: float


class SiteResponse(BaseModel):
    id: int
    name: str
    location: str
    latitude: float
    longitude: float
    created_at: datetime

    class Config:
        from_attributes = True