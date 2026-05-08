from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    Trainer,
    TrainingArguments
)

from datasets import Dataset
import pandas as pd

MODEL_NAME = "prithivida/grammar_error_correcter_v1"


def train_model(csv_path: str):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, use_fast=False)

    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME, use_safetensors=False)

    df = pd.read_csv(csv_path)

    dataset = Dataset.from_pandas(df)


    def preprocess(example):
        inputs = tokenizer(
            example["source"],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        targets = tokenizer(
            example["target"],
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        inputs["labels"] = targets["input_ids"]

        return inputs

    tokenized = dataset.map(preprocess)

    args = TrainingArguments(
        output_dir="models_saved/bert-gec",
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=500,
        logging_steps=100,
        learning_rate=2e-5,
        weight_decay=0.01
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized
    )

    trainer.train()

    model.save_pretrained("models_saved/bert-gec")
    tokenizer.save_pretrained("models_saved/bert-gec")
