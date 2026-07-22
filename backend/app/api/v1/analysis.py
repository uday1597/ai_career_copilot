from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.job import Job
from app.models.resume import Resume
from app.schemas.analysis import MatchRequest
from app.services.ingestion.match_service import calculate_match
from app.services.ai.matching import match_resume_to_jobs
from app.services.ai.assessment_generator import generate_assessment
from app.models.skill_assessment import SkillAssessment
from app.schemas.assessment import AssessmentGenerateRequest

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

@router.get("/match/{resume_id}")
def match_resume(
    resume_id: str,
    db: Session = Depends(get_db)
):
    return match_resume_to_jobs(
        db,
        resume_id
    )
    
@router.post("/generate")
def generate_skill_assessment(
    payload: AssessmentGenerateRequest,
    db: Session = Depends(get_db)
):
    assessment = generate_assessment(
        payload.skill
    )

    record = SkillAssessment(
        resume_id=payload.resume_id,
        job_id=payload.job_id,
        skill=payload.skill,
        questions=assessment
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record