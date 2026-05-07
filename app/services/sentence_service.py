import nltk

nltk.download("punkt")


def split_sentences(text: str):
    sentences = nltk.sent_tokenize(text)

    return [s.strip() for s in sentences if len(s.strip()) > 0]
