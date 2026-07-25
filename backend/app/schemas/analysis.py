

from uuid import UUID

from pydantic import BaseModel

class MatchRequest(BaseModel):
    resume_id: str
    job_id: str
    
class MatchResponse(BaseModel):

    id: UUID

    resume_id: UUID

    job_id: UUID

    match_score: int

    matching_technologies: list[str]

    missing_technologies: list[str]

    ai_explanation: dict

    model_config = {
        "from_attributes": True
    }