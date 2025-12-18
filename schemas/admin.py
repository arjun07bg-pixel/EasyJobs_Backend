from pydantic import BaseModel

class AdminCreate(BaseModel):
    admin_name: str
    email: str
    password: str

class AdminOut(BaseModel):
    admin_id: int
    admin_name: str
    email: str

    class Config:
        from_attributes = True
