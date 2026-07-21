from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.job import Job
from app.models.resume import Resume
from app.schemas.analysis import MatchRequest
from app.services.ingestion.match_service import calculate_match

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


@router.post("/match")
def match_resume_to_job(
    payload: MatchRequest,
    db: Session = Depends(get_db)
):

    resume = db.get(
        Resume,
        payload.resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    job = db.get(
        Job,
        payload.job_id
    )

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return calculate_match(
        resume.technologies or [],
        job.technologies or []
    )