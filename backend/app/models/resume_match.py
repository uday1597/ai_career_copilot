import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class ResumeMatch(Base):

    __tablename__ = "resume_matches"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    resume_id = Column(
        UUID(as_uuid=True),
        ForeignKey("resumes.id"),
        nullable=False
    )

    job_id = Column(
        UUID(as_uuid=True),
        ForeignKey("jobs.id"),
        nullable=False
    )

    match_score = Column(
        Integer,
        nullable=False
    )

    matching_technologies = Column(
        JSON,
        nullable=False
    )

    missing_technologies = Column(
        JSON,
        nullable=False
    )

    ai_explanation = Column(
        JSON,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )