from datetime import datetime
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.assessment import Assessment
from app.models.learning_roadmap import LearningRoadmap
from app.models.resume_match import ResumeMatch

from app.schemas.assessment import (
    AssessmentGenerateRequest,
    AssessmentResponse,
    AssessmentStatusResponse,
    AssessmentSubmitRequest,
)

from app.services.ai.assessment_generator import (
    generate_assessment,
)
from app.services.ai.assessment_evaluator import evaluate_assessment

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)


@router.post(
    "/generate",
    response_model=AssessmentResponse,
)
def generate(
    payload: AssessmentGenerateRequest,
    db: Session = Depends(get_db),
):

    existing = (
        db.query(Assessment)
        .filter(
            Assessment.match_id == payload.match_id,
            Assessment.week == payload.week,
        )
        .first()
    )

    if existing:
        return existing

    match = db.get(
        ResumeMatch,
        payload.match_id,
    )

    if not match:
        raise HTTPException(
            status_code=404,
            detail="Match not found",
        )

    roadmap = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == payload.match_id
        )
        .first()
    )

    if not roadmap:
        raise HTTPException(
            status_code=404,
            detail="Learning roadmap not found",
        )

    week = next(
        (
            w
            for w in roadmap.roadmap["weeks"]
            if w["week"] == payload.week
        ),
        None,
    )

    if not week:
        raise HTTPException(
            status_code=404,
            detail="Roadmap week not found",
        )

    questions = generate_assessment(
        week
    )

    record = Assessment(
        match_id=payload.match_id,
        week=payload.week,
        questions=questions,
        status="NOT_STARTED",
    )

    db.add(record)

    db.commit()

    db.refresh(record)

    return record

@router.get(
    "/result/{assessment_id}",
    response_model=AssessmentResponse,
)
def get_result(
    assessment_id: UUID,
    db: Session = Depends(get_db),
):
    assessment = db.get(
        Assessment,
        assessment_id,
    )

    if not assessment:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found",
        )

    return assessment
    
@router.get("/match/{match_id}")
def assessment_history(
    match_id: UUID,
    db: Session = Depends(get_db),
):

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.match_id == match_id
        )
        .order_by(
            Assessment.week
        )
        .all()
    )

    return [
        {
            "week": a.week,
            "status": a.status,
            "overall_score": a.overall_score,
            "completed_at": a.completed_at,
        }
        for a in assessments
    ]

@router.get(
    "/{match_id}/{week}",
    response_model=AssessmentResponse,
)
def get_assessment(
    match_id: UUID,
    week: int,
    db: Session = Depends(get_db),
):

    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.match_id == match_id,
            Assessment.week == week,
        )
        .first()
    )

    if not assessment:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found",
        )

    return assessment


@router.post(
    "/submit",
    response_model=AssessmentResponse,
)
def submit_assessment(
    payload: AssessmentSubmitRequest,
    db: Session = Depends(get_db),
):

    assessment = db.get(
        Assessment,
        payload.assessment_id,
    )

    if not assessment:
        raise HTTPException(
            status_code=404,
            detail="Assessment not found",
        )

    assessment.mcq_answers = payload.mcq_answers
    assessment.coding_answers = payload.coding_answers
    assessment.scenario_answer = payload.scenario_answer

    assessment.status = "COMPLETED"

    assessment.completed_at = datetime.utcnow()

    mcqs = assessment.questions["mcqs"]

    score = 0

    for i, question in enumerate(mcqs):

        if (
            i < len(payload.mcq_answers)
            and payload.mcq_answers[i] == question["answer"]
        ):
            score += 1

    mcq_score = round(
        score / len(mcqs) * 100
    )

    feedback = evaluate_assessment(

        assessment.questions,

        mcq_score,

        payload.coding_answers,

        payload.scenario_answer,

    )

    assessment.mcq_score = mcq_score

    assessment.coding_score = feedback["coding_score"]

    assessment.scenario_score = feedback["scenario_score"]

    assessment.overall_score = feedback["overall_score"]

    assessment.feedback = feedback

    assessment.status = "COMPLETED"

    db.commit()

    db.refresh(assessment)

    return assessment

@router.get(
    "/status/{match_id}/{week}",
    response_model=AssessmentStatusResponse,
)
def assessment_status(
    match_id: UUID,
    week: int,
    db: Session = Depends(get_db),
):

    assessment = (
        db.query(Assessment)
        .filter(
            Assessment.match_id == match_id,
            Assessment.week == week,
        )
        .order_by(
            Assessment.created_at.desc()
        )
        .first()
    )

    if not assessment:

        return {
            "exists": False
        }

    return {
        "exists": True,
        "assessment_id": str(assessment.id),
        "status": assessment.status,
        "overall_score": assessment.overall_score,
        "completed_at": assessment.completed_at,
    }

@router.post(
    "/new-attempt",
    response_model=AssessmentResponse,
)
def new_attempt(
    payload: AssessmentGenerateRequest,
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
    roadmap = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == payload.match_id
        )
        .first()
    )
    week = next(
        (
            w
            for w in roadmap.roadmap["weeks"]
            if w["week"] == payload.week
        ),
        None,
    )
    questions = generate_assessment(
        week
    )
    record = Assessment(

        match_id=payload.match_id,

        week=payload.week,

        questions=questions,

        status="NOT_STARTED",

    )
    db.add(record)

    db.commit()

    db.refresh(record)

    return record