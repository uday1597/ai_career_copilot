from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class UserCreate(BaseModel):
    email: EmailStr
    password: str

    first_name: str | None = None
    last_name: str | None = None


class UserResponse(BaseModel):
    id: UUID

    email: EmailStr

    first_name: str | None = None
    last_name: str | None = None

    created_at: datetime


    model_config = ConfigDict(
        from_attributes=True
    )