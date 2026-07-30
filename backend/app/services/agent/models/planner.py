from enum import Enum

from pydantic import BaseModel


class PlanTool(str, Enum):
    DASHBOARD = "get_dashboard"
    SEARCH_JOBS = "search_jobs"
    RESUME_MATCH = "get_resume_match"
    ROADMAP = "get_learning_roadmap"
    ASSESSMENT = "get_assessment"


class PlanStep(BaseModel):
    tool: PlanTool
    reason: str


class ExecutionPlan(BaseModel):
    steps: list[PlanStep]