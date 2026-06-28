from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: str
    filename: str
    summary: str | None = None

    model_config = {
        "from_attributes": True
    }