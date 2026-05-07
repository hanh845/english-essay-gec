import uuid
from sqlalchemy.orm import Session
from app.ml.inference import correct_sentence
from app.models.prediction import Prediction

ERROR_TYPES = {
    "spelling": ["teh", "recieve", "goood"],
    "grammar": ["goed", "he go"]
}


def detect_error_type(original, corrected):
    if original.lower() != corrected.lower():
        return "grammar_or_spelling"

    return "clean"


def predict_sentence(
        db: Session,
        sentence_id: str,
        content: str,
        model_id: str
):
    corrected = correct_sentence(content)

    label = 0

    if corrected != content:
        label = 1

    confidence = 0.95

    prediction = Prediction(
        prediction_id=str(uuid.uuid4()),
        sentence_id=sentence_id,
        model_id=model_id,
        label=label,
        confidence=confidence,
        original_text=content,
        corrected_text=corrected,
        error_type=detect_error_type(content, corrected)
    )

    db.add(prediction)
    db.commit()

    return prediction
