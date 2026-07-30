from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.resume import Resume
from app.models.job import Job
from app.models.resume_match import ResumeMatch
from app.models.learning_roadmap import LearningRoadmap
from app.models.assessment import Assessment

from app.schemas.profile import (
    ProfileResponse,
    ProfileSummary,
    CareerStats,
    LatestMatch,
    RoadmapSummary,
    AssessmentSummary,
)

router = APIRouter(
    prefix="/profile",
    tags=["Profile"],
)


@router.get(
    "",
    response_model=ProfileResponse,
)
def get_profile(
    db: Session = Depends(get_db),
):

    latest_resume = (
        db.query(Resume)
        .order_by(Resume.created_at.desc())
        .first()
    )

    latest_match = (
        db.query(ResumeMatch)
        .order_by(ResumeMatch.created_at.desc())
        .first()
    )

    latest_match_response = None

    if latest_match:

        job = db.get(Job, latest_match.job_id)

        latest_match_response = LatestMatch(
            job_title=job.title,
            company=job.company,
            match_score=latest_match.match_score,
            missing_skills=latest_match.missing_technologies or [],
        )

    roadmap = None

    if latest_match:
        roadmap = (
            db.query(LearningRoadmap)
            .filter(
                LearningRoadmap.match_id == latest_match.id
            )
            .first()
        )

    roadmap_response = None

    if roadmap:

        weeks = roadmap.roadmap.get("weeks", [])

        completed = (
            db.query(Assessment)
            .filter(
                Assessment.match_id == latest_match.id,
                Assessment.status == "COMPLETED",
            )
            .count()
        )

        total = len(weeks)

        current = min(completed + 1, total) if total else 0

        progress = (
            int((completed / total) * 100)
            if total
            else 0
        )

        roadmap_response = RoadmapSummary(
            current_week=current,
            completed_weeks=completed,
            total_weeks=total,
            progress=progress,
        )

    completed_assessments = (
        db.query(Assessment)
        .filter(Assessment.status == "COMPLETED")
        .all()
    )

    scores = [
        assessment.overall_score
        for assessment in completed_assessments
        if assessment.overall_score is not None
    ]

    assessment_response = AssessmentSummary(
        completed=len(completed_assessments),
        average_score=(
            int(sum(scores) / len(scores))
            if scores
            else 0
        ),
        highest_score=max(scores) if scores else 0,
    )

    profile = ProfileSummary(
        resume_filename=latest_resume.filename if latest_resume else "",
        summary=latest_resume.summary if latest_resume else "",
        skills=latest_resume.technologies if latest_resume else [],
        resume_uploaded_at=latest_resume.created_at if latest_resume else None,
    )

    stats = CareerStats(
        resumes=db.query(Resume).count(),
        jobs=db.query(Job).count(),
        matches=db.query(ResumeMatch).count(),
        roadmaps=db.query(LearningRoadmap).count(),
        assessments=db.query(Assessment).count(),
    )

    return ProfileResponse(
        profile=profile,
        stats=stats,
        latest_match=latest_match_response,
        roadmap=roadmap_response,
        assessment=assessment_response,
    )