from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str

class UserOut(BaseModel):
    user_id: int
    user_name: str
    email: str

    class Config:
        from_attributes = True





