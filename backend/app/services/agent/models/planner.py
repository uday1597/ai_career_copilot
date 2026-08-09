from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class PlanTool(str, Enum):
    DASHBOARD = "get_dashboard"
    SEARCH_JOBS = "search_jobs"
    RESUME_MATCH = "get_resume_match"
    ROADMAP = "get_learning_roadmap"
    ASSESSMENT = "get_assessment"

class PlanStep(BaseModel):
    tool: str
    reason: str
    source: Literal["internal", "mcp"]
    arguments: dict = Field(default_factory=dict)


class ExecutionPlan(BaseModel):
    steps: list[PlanStep]