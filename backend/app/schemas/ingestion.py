from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    title: str = Field(..., min_length=1)
    source: str = Field(..., min_length=1)
    document_type: str = Field(..., min_length=1)
    text: str = Field(..., min_length=1)