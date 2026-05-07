from fastapi import APIRouter

from app.ml.train_bert_gec import train_model

router = APIRouter()


@router.post("/train/lang8")
def train_lang8_model():
    train_model("data/lang8/lang8.csv")

    return {
        "message": "Training completed"
    }
