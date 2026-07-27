from sqlalchemy.orm import Session

from app.models.job import Job
from app.models.resume_match import ResumeMatch
from app.models.learning_roadmap import LearningRoadmap
from app.models.assessment import Assessment

from app.schemas.dashboard import (
    DashboardResponse,
    LatestMatch,
    NextAction,
    RoadmapSummary,
    AssessmentSummary,
    SkillSummary,
)


def build_dashboard(
    db: Session,
):

    latest_match = (
        db.query(ResumeMatch)
        .order_by(
            ResumeMatch.created_at.desc()
        )
        .first()
    )

    if not latest_match:

        return DashboardResponse(

            status="UPLOAD_RESUME",

            next_action=NextAction(

                title="Upload Resume",

                url="/resume",

            )

        )

    job = db.get(
        Job,
        latest_match.job_id,
    )

    roadmap = (
        db.query(LearningRoadmap)
        .filter(
            LearningRoadmap.match_id == latest_match.id
        )
        .first()
    )

    if roadmap is None:

        return DashboardResponse(

            status="GENERATE_ROADMAP",

            next_action=NextAction(

                title="Generate Learning Roadmap",

                url="/roadmap",

            ),

            latest_match=LatestMatch(

                job_title=job.title,
                match_score=latest_match.match_score,

            ),

        )

    assessments = (
        db.query(Assessment)
        .filter(
            Assessment.match_id == latest_match.id
        )
        .all()
    )

    if len(assessments) == 0:

        status = "START_ASSESSMENT"

        next_action = NextAction(

            title="Start Week 1 Assessment",

            url="/roadmap",

        )

    elif any(
        a.status == "IN_PROGRESS"
        for a in assessments
    ):

        current = next(
            a
            for a in assessments
            if a.status == "IN_PROGRESS"
        )

        status = "IN_PROGRESS"

        next_action = NextAction(

            title=f"Continue Week {current.week}",

            url=f"/assessment?matchId={latest_match.id}&week={current.week}",

        )

    else:

        status = "COMPLETED"

        next_week = min(
            len(assessments) + 1,
            len(roadmap.roadmap["weeks"]),
        )

        next_action = NextAction(

            title=f"Start Week {next_week} Assessment",

            url="/roadmap",

        )

    total_weeks = len(
        roadmap.roadmap["weeks"]
    )

    completed = sum(
        1
        for a in assessments
        if a.status == "COMPLETED"
    )

    in_progress = sum(
        1
        for a in assessments
        if a.status == "IN_PROGRESS"
    )

    not_started = (
        total_weeks
        - completed
        - in_progress
    )

    completion = (
        round(
            completed
            / total_weeks
            * 100
        )
        if total_weeks
        else 0
    )

    attempted = len(assessments)

    scores = [
        a.overall_score
        for a in assessments
        if a.overall_score is not None
    ]

    average_score = (
        round(
            sum(scores)
            / len(scores)
        )
        if scores
        else 0
    )

    best_score = (
        max(scores)
        if scores
        else 0
    )

    return DashboardResponse(

        status=status,

        next_action=next_action,

        latest_match=LatestMatch(

            job_title=job.title,
            match_score=latest_match.match_score,

        ),

        roadmap=RoadmapSummary(

            total_weeks=total_weeks,

            completed_weeks=completed,

            in_progress_weeks=in_progress,

            not_started_weeks=not_started,

            completion_percentage=completion,

        ),

        assessments=AssessmentSummary(

            attempted=attempted,

            average_score=average_score,

            best_score=best_score,

        ),

        skills=SkillSummary(

            strongest=latest_match.matching_technologies,

            weakest=latest_match.missing_technologies,

        ),

    )