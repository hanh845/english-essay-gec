import pandas as pd
from datasets import Dataset


def load_lang8_dataset(csv_path: str):
    df = pd.read_csv(csv_path)

    df = df[["source", "target"]]

    dataset = Dataset.from_pandas(df)

    return dataset
