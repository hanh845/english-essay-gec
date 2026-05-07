from sqlalchemy import Column, String, Text, Integer, Boolean
from app.core.database import Base


class Sentence(Base):
    __tablename__ = "sentences"
    __table_args__ = {"schema": "db_assignment"}

    sentence_id = Column(String, primary_key=True)
    version_id = Column(String)
    content = Column(Text)
    position = Column(Integer)
    is_clean = Column(Boolean)

