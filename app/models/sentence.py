from sqlalchemy import (
    Column,
    Text,
    Integer,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from datetime import datetime
import uuid

from app.core.database import Base


class Sentence(Base):
    __tablename__ = "sentences"

    sentence_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    document_id = Column(
        UUID(as_uuid=True),
        ForeignKey("documents.document_id", ondelete="CASCADE"),
        nullable=False
    )

    version_id = Column(
        UUID(as_uuid=True),
        ForeignKey("document_versions.version_id"),
        nullable=True
    )

    content = Column(
        Text,
        nullable=False
    )

    position = Column(
        Integer,
        nullable=True
    )

    is_clean = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # =========================
    # Relationships
    # =========================

    document = relationship(
        "Document",
        back_populates="sentences"
    )

    predictions = relationship(
        "Prediction",
        back_populates="sentence",
        cascade="all, delete-orphan"
    )
