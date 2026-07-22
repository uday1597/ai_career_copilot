import uuid

from sqlalchemy import JSON, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class SkillAssessment(Base):
    __tablename__ = "skill_assessments"

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    resume_id: Mapped[str]

    job_id: Mapped[str]

    skill: Mapped[str]

    questions: Mapped[list] = mapped_column(
        JSON
    )

    score: Mapped[int | None] = mapped_column(
        nullable=True
    )

    completed: Mapped[bool] = mapped_column(
        default=False
    )

    feedback: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )