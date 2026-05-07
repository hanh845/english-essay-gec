from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM

import torch

MODEL_PATH = "models_saved/bert-gec"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)


def correct_sentence(sentence: str):
    input_text = f"gec: {sentence}"

    inputs = tokenizer.encode(
        input_text,
        return_tensors="pt"
    )

    outputs = model.generate(
        inputs,
        max_length=128,
        num_beams=4,
        early_stopping=True
    )

    corrected = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return corrected
