import uuid

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import JSON
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

from app.db.database import Base

class Assessment(Base):

    __tablename__ = "assessments"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    match_id = Column(
        UUID(as_uuid=True),
        ForeignKey("resume_matches.id"),
        nullable=False,
    )

    week = Column(
        Integer,
        nullable=False,
    )

    questions = Column(
        JSON,
        nullable=False,
    )

    mcq_answers = Column(
        JSON,
        nullable=True,
    )

    coding_answers = Column(
        JSON,
        nullable=True,
    )

    scenario_answer = Column(
        Text,
        nullable=True,
    )

    mcq_score = Column(Integer, nullable=True)

    coding_score = Column(Integer, nullable=True)

    scenario_score = Column(Integer, nullable=True)

    overall_score = Column(Integer, nullable=True)

    feedback = Column(JSON, nullable=True)

    status = Column(
        String,
        default="NOT_STARTED",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    completed_at = Column(
        DateTime(timezone=True),
        nullable=True,
    )