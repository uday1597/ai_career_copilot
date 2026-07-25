from uuid import UUID

from pydantic import BaseModel


class RoadmapGenerateRequest(BaseModel):
    match_id: UUID


class RoadmapResponse(BaseModel):

    id: UUID

    match_id: UUID

    roadmap: dict

    model_config = {
        "from_attributes": True
    }