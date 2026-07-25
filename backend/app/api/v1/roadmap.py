from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from uuid import UUID
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.resume import Resume
from app.models.job import Job
from app.models.learning_roadmap import LearningRoadmap

from app.schemas.roadmap import RoadmapGenerateRequest
from app.schemas.roadmap import RoadmapResponse

from app.services.ai.learning_roadmap import generate_learning_roadmap
from app.models.resume_match import ResumeMatch

router = APIRouter(
    prefix="/roadmap",
    tags=["Roadmap"]
)

@router.post(
    "/generate",
    response_model=RoadmapResponse,
)
def generate(
    payload: RoadmapGenerateRequest,
    db: Session = Depends(get_db),
):

    match = db.get(
        ResumeMatch,
        payload.match_id,
    )

    if not match:
        raise HTTPException(
            status_code=404,
            detail="Match not found",
        )

    existing = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == payload.match_id
        )
        .first()
    )

    if existing:
        return existing

    roadmap = generate_learning_roadmap(
        match.match_score,
        match.matching_technologies,
        match.missing_technologies,
        match.ai_explanation,
    )

    record = LearningRoadmap(
        match_id=match.id,
        roadmap=roadmap,
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record

@router.get(
    "/{match_id}",
    response_model=RoadmapResponse,
)
def get_roadmap(
    match_id: UUID,
    db: Session = Depends(get_db),
):

    roadmap = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == match_id
        )
        .first()
    )

    if not roadmap:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found",
        )

    return roadmap