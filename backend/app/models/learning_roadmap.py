import uuid

from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.sql import func

from app.db.database import Base

class LearningRoadmap(Base):

    __tablename__ = "learning_roadmaps"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    match_id = Column(
        UUID(as_uuid=True),
        ForeignKey("resume_matches.id"),
        nullable=False
    )

    roadmap = Column(
        JSON,
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )