from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID


class URLRequest(BaseModel):
    url: str
    expiry: Optional[datetime] = None


class URLResponse(BaseModel):
    id: UUID
    url: str
    short_key: str
    created_at: datetime
    expiry_date: Optional[datetime] = None

    class Config:
        orm_mode = True
