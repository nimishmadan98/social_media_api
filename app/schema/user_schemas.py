from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserSchema(BaseModel):
    name: str
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
