from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.core.database import Base


class DocumentVersion(Base):
    __tablename__ = "document_versions"

    version_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    document_id = Column(
        UUID(as_uuid=True),
        ForeignKey("documents.document_id"),
        nullable=False
    )

    extracted_text = Column(Text, nullable=True)

    extraction_method = Column(String(100), nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # relationship
    document = relationship(
        "Document",
        back_populates="versions"
    )
