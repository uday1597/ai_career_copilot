from datetime import datetime

from pydantic import BaseModel


class ProfileSummary(BaseModel):
    resume_filename: str
    summary: str | None = None
    skills: list[str]
    resume_uploaded_at: datetime | None = None


class CareerStats(BaseModel):
    resumes: int
    jobs: int
    matches: int
    roadmaps: int
    assessments: int


class LatestMatch(BaseModel):
    job_title: str
    company: str
    match_score: float
    missing_skills: list[str]


class RoadmapSummary(BaseModel):
    current_week: int
    completed_weeks: int
    total_weeks: int
    progress: int


class AssessmentSummary(BaseModel):
    completed: int
    average_score: int
    highest_score: int


class ProfileResponse(BaseModel):
    profile: ProfileSummary
    stats: CareerStats
    latest_match: LatestMatch | None = None
    roadmap: RoadmapSummary | None = None
    assessment: AssessmentSummary