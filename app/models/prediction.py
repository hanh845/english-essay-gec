from sqlalchemy import Column, String, Text, Float, Integer
from app.core.database import Base


class Prediction(Base):
    __tablename__ = "predictions"
    __table_args__ = {"schema": "db_assignment"}

    prediction_id = Column(String, primary_key=True)
    sentence_id = Column(String)
    model_id = Column(String)
    label = Column(Integer)
    confidence = Column(Float)
    original_text = Column(Text)
    corrected_text = Column(Text)
    error_type = Column(String)
