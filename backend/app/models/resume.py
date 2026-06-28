import uuid

from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import Text, JSON, DateTime
from app.db.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    filename: Mapped[str]

    extracted_text: Mapped[str] = mapped_column(Text)

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    technologies: Mapped[list | None] = mapped_column(
        JSON,
        nullable=True
    )
    extraction_method: Mapped[str | None] = mapped_column(
    nullable=True
    )

    page_count: Mapped[int | None] = mapped_column(
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )