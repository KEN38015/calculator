from datetime import datetime

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str


class ItemOut(BaseModel):
    id: int
    name: str
    created_at: datetime

    class Config:
        from_attributes = True
