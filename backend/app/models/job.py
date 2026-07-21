import uuid
from sqlalchemy import Text, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from pgvector.sqlalchemy import Vector

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    title: Mapped[str]

    description: Mapped[str] = mapped_column(
        Text
    )

    technologies: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True
    )
    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(1536),
        nullable=True
    )