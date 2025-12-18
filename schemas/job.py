from pydantic import BaseModel

class JobCreate(BaseModel):
    job_title: str
    post_id: int
    user_id: int

class JobOut(JobCreate):
    job_id: int

    class Config:
        from_attributes = True
