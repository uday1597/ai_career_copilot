from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.job import Job
from app.schemas.job import JobCreate
from app.services.ai.job_analyzer import analyze_job

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/")
def get_jobs(
    db: Session = Depends(get_db)
):
    return db.query(Job).all()
    
@router.post("/")
def create_job(
    payload: JobCreate,
    db: Session = Depends(get_db)
):
    analysis = analyze_job(
        payload.description
    )

    job = Job(
        title=payload.title,
        description=payload.description,
        technologies=analysis["technologies"]
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job