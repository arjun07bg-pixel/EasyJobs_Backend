from pydantic import BaseModel

class CompanyCreate(BaseModel):
    company_name: str
    location: str

class CompanyOut(CompanyCreate):
    company_id: int

    class Config:
        from_attributes = True
