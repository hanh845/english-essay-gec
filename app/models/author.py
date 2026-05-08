from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from datetime import datetime
import uuid

from app.core.database import Base
from app.models.document_author import document_authors


class Author(Base):
    __tablename__ = "authors"

    author_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    # relationships
    documents = relationship(
        "Document",
        secondary=document_authors,
        back_populates="authors"
    )
