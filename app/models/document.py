from sqlalchemy import Column, String, Text, TIMESTAMP
from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"
    __table_args__ = {"schema": "db_assignment"}

    document_id = Column(String, primary_key=True)
    title = Column(Text)
    file_type = Column(String)
    file_path = Column(Text)
    created_at = Column(TIMESTAMP)
