from sqlalchemy import Column, Integer, String, ForeignKey
from database.database import Base

class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    job_id = Column(Integer, nullable=False)
    resume = Column(String, nullable=False)
    company_id = Column(Integer, nullable=False)




