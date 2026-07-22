from pydantic import BaseModel


class AssessmentGenerateRequest(BaseModel):
    resume_id: str
    job_id: str
    skill: str


class AssessmentGenerateResponse(BaseModel):
    id: str
    resume_id: str
    job_id: str
    skill: str
    completed: bool
    score: int | None
    questions: dict


class AssessmentSubmitRequest(BaseModel):
    assessment_id: str
    answers: dict