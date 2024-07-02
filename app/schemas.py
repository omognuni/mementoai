from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class URLRequest(BaseModel):
    url: str
    expiry_date: Optional[datetime] = None


class URLResponse(BaseModel):
    id: UUID
    url: str
    short_key: str
    created_at: datetime
    expiry_date: Optional[datetime] = None
    stats: int

    class Config:
        orm_mode = True


class URLStats(BaseModel):
    url: str
    short_key: str
    stats: int

    class Config:
        orm_mode = True
