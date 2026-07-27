from uuid import UUID

from pydantic import BaseModel, ConfigDict


class JobCreate(BaseModel):

    title: str

    company: str

    location: str | None = None

    description: str

class JobResponse(BaseModel):

    id: UUID

    title: str

    company: str

    location: str | None

    description: str

    technologies: list[str]

    model_config = ConfigDict(
        from_attributes=True
    )
