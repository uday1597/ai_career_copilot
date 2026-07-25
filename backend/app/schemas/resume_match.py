from pydantic import BaseModel


class ResumeMatchResponse(BaseModel):

    id: str

    resume_id: str

    job_id: str

    match_score: int

    matching_technologies: list[str]

    missing_technologies: list[str]

    ai_explanation: dict

    model_config = {
        "from_attributes": True
    }