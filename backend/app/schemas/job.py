from pydantic import BaseModel


class JobCreate(BaseModel):
    title: str
    description: str


class JobResponse(BaseModel):
    id: str
    title: str

    model_config = {
        "from_attributes": True
    }