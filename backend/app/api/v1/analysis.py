from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.job import Job
from app.models.resume import Resume
from app.models.resume_match import ResumeMatch

from app.schemas.analysis import (
    MatchRequest,
    MatchResponse,
)

from app.services.ingestion.match_service import calculate_match
from app.services.ai.match_explainer import explain_match

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"],
)


@router.post(
    "/match",
    response_model=MatchResponse,
)
def match_resume(
    payload: MatchRequest,
    db: Session = Depends(get_db),
):

    resume = db.get(
        Resume,
        payload.resume_id,
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    job = db.get(
        Job,
        payload.job_id,
    )

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found",
        )

    result = calculate_match(
        resume,
        job,
    )

    explanation = explain_match(
        resume_summary=resume.summary,
        resume_technologies=resume.technologies,
        job_title=job.title,
        job_description=job.description,
        job_technologies=job.technologies,
        match_score=result["match_score"],
        matching_technologies=result["matching_technologies"],
        missing_technologies=result["missing_technologies"],
    )

    record = ResumeMatch(
        resume_id=resume.id,
        job_id=job.id,
        match_score=result["match_score"],
        matching_technologies=result["matching_technologies"],
        missing_technologies=result["missing_technologies"],
        ai_explanation=explanation,
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record


@router.get(
    "/latest/{resume_id}",
    response_model=MatchResponse,
)
def latest_match(
    resume_id: str,
    db: Session = Depends(get_db),
):

    match = (
        db.query(ResumeMatch)
        .filter(
            ResumeMatch.resume_id == resume_id
        )
        .order_by(
            ResumeMatch.created_at.desc()
        )
        .first()
    )

    if not match:
        raise HTTPException(
            status_code=404,
            detail="No match found",
        )

    return match