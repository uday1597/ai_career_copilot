from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobResponse
from app.services.ai.job_analyzer import analyze_job

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get(
    "/",
    response_model=list[JobResponse]
)
def get_jobs(
    db: Session = Depends(get_db)
):
    jobs = (
        db.query(Job)
        .all()
    )

    return [
        JobResponse(
            id=str(job.id),
            title=job.title,
            description=job.description,
            technologies=job.technologies,
        )
        for job in jobs
    ]
    
@router.post("/")
def create_job(
    payload: JobCreate,
    db: Session = Depends(get_db)
):
    print("=" * 100)
    print(payload.description)
    print("=" * 100)
    analysis,embedding = analyze_job(
        payload.description
    )

    job = Job(
        title=payload.title,
        description=payload.description,
        technologies=analysis["technologies"],
        embedding=embedding
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job