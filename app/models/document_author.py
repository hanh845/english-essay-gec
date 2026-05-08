from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.core.database import Base

document_authors = Table(
    "document_authors",
    Base.metadata,

    Column(
        "author_id",
        UUID(as_uuid=True),
        ForeignKey("authors.author_id")
    ),

    Column(
        "document_id",
        UUID(as_uuid=True),
        ForeignKey("documents.document_id")
    )
)
