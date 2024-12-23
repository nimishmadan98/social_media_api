from typing import Optional
from pydantic import BaseModel

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    likes_count: Optional[int] = 0
    comments_count: Optional[int] = 0

    class Config:
        orm_mode = True
        from_attributes = True
