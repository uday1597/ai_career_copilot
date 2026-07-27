from pydantic import BaseModel


class NextAction(BaseModel):

    title: str

    url: str


class LatestMatch(BaseModel):

    job_title: str

    # company: str

    match_score: int


class RoadmapSummary(BaseModel):

    total_weeks: int

    completed_weeks: int

    in_progress_weeks: int

    not_started_weeks: int

    completion_percentage: int


class AssessmentSummary(BaseModel):

    attempted: int

    average_score: int

    best_score: int


class SkillSummary(BaseModel):

    strongest: list[str]

    weakest: list[str]


class DashboardResponse(BaseModel):

    status: str

    next_action: NextAction

    latest_match: LatestMatch | None = None

    roadmap: RoadmapSummary | None = None

    assessments: AssessmentSummary | None = None

    skills: SkillSummary | None = None