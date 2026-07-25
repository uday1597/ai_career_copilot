from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class ResumeResponse(BaseModel):
    id: UUID

    filename: str
    file_path: str

    extracted_text: str

    summary: str | None = None

    technologies: list | None = None

    extraction_method: str | None = None

    page_count: int | None = None

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )