from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from models.job import Job
from schemas.job import JobCreate, JobOut

router = APIRouter(prefix="/jobs", tags=["Jobs"])

from models.post import Post
from models.user import User

@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db)):

    post = db.query(Post).filter(Post.post_id == job.post_id).first()
    if not post:
        raise HTTPException(status_code=400, detail="Post not found")

    user = db.query(User).filter(User.user_id== job.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    new_job = Job(
        job_title=job.job_title,
        post_id=job.post_id,
        user_id=job.user_id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job




@router.get("/", response_model=list[JobOut])
def get_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()



@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.job_id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job



@router.put("/{job_id}", response_model=JobOut)
def update_job(job_id: int, job: JobCreate, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.job_id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db_job.job_title = job.job_title
    db_job.post_id = job.post_id
    db_job.user_id = job.user_id
    db.commit()
    db.refresh(db_job)
    return db_job 




@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.query(Job).filter(Job.job_id == job_id).first()
    if not db_job:
        raise HTTPException(status_code=404, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return {"detail": "Job deleted successfully"}
