from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int
    company_id: int
    resume: str  

class ApplicationOut(BaseModel):
    application_id: int
    user_id: int
    job_id: int
    company_id: int
    resume: str

    class Config:
        from_attributes = True
