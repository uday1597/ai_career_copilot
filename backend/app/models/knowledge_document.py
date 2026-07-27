import uuid

from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

from pgvector.sqlalchemy import Vector

from app.db.database import Base

class KnowledgeDocument(Base):

    __tablename__ = "knowledge_documents"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    title: Mapped[str] = mapped_column(
        String(255),
    )

    source: Mapped[str] = mapped_column(
        String(255),
    )

    document_type: Mapped[str] = mapped_column(
        String(100),
    )

    chunk_index: Mapped[int]

    content: Mapped[str] = mapped_column(
        Text,
    )

    embedding: Mapped[list[float] | None] = mapped_column(
        Vector(1536),
        nullable=True,
    )

    created_at: Mapped = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )