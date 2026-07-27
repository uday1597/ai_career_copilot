from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class AssessmentGenerateRequest(BaseModel):
    match_id: UUID
    week: int


class AssessmentSubmitRequest(BaseModel):
    assessment_id: UUID
    mcq_answers: list[int]
    coding_answers: list[str]
    scenario_answer: str


class MCQ(BaseModel):
    id: int
    question: str
    options: list[str]
    answer: int
    explanation: str


class CodingQuestion(BaseModel):
    id: int
    title: str
    question: str
    difficulty: str
    expected_skills: list[str]
    hints: list[str]


class ScenarioQuestion(BaseModel):
    id: int
    question: str
    expected_points: list[str]
    sample_answer: str


class AssessmentQuestions(BaseModel):
    title: str
    estimated_duration: str
    difficulty: str
    mcqs: list[MCQ]
    coding: list[CodingQuestion]
    scenario: list[ScenarioQuestion]


class AssessmentResponse(BaseModel):

    id: UUID

    match_id: UUID

    week: int

    questions: AssessmentQuestions

    mcq_answers: list[int] | None = None

    coding_answers: list[str] | None = None

    scenario_answer: str | None = None

    mcq_score: int | None = None

    coding_score: int | None = None

    scenario_score: int | None = None

    overall_score: int | None = None

    feedback: dict[str, Any] | None = None

    status: str

    model_config = ConfigDict(
        from_attributes=True
    )

class AssessmentStatusResponse(BaseModel):

    exists: bool

    assessment_id: UUID | None = None

    status: str | None = None

    overall_score: int | None = None

    completed_at: datetime | None = None