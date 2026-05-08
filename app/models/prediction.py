from sqlalchemy import Column, Integer, Float, Text, ForeignKey, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid

from app.core.database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    prediction_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    sentence_id = Column(
        UUID(as_uuid=True),
        ForeignKey("sentences.sentence_id"),
        nullable=False
    )
    model_id = Column(String, nullable=True)

    label = Column(Integer, nullable=False)

    confidence = Column(Float, nullable=True)

    corrected_text = Column(Text, nullable=True)

    original_text = Column(Text, nullable=True)

    error_type = Column(String, nullable=True)

    predicted_at = Column(DateTime(timezone=True), server_default=func.now())

    # relationship
    sentence = relationship(
        "Sentence",
        back_populates="predictions"
    )
