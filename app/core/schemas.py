
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ImageBase(BaseModel):
    filename: str

class ImageCreate(ImageBase):
    pass

class Image(ImageBase):
    id: int
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
