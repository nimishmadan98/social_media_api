from pydantic import BaseModel

class LikeCreate(BaseModel):
    user_id: int

class LikeOut(BaseModel):
    id: int
    user_id: int
    post_id: int

    class Config:
        orm_mode = True
