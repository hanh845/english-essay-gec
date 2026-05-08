from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"

    document_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    title = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    file_type = Column(String(100), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # relationship sentences
    sentences = relationship(
        "Sentence",
        back_populates="document",
        cascade="all, delete-orphan"
    )

    # relationship document_versions
    versions = relationship(
        "DocumentVersion",
        back_populates="document",
        cascade="all, delete-orphan"
    )
