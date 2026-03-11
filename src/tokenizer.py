import re


class SimpleTokenizer:
    """
    A simple regex-based tokenizer that converts text to token IDs
    and token IDs back to text.
    """

    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        tokens = re.split(r'([,.!?;:"()\'"]|--|\s)', text)
        tokens = [token.strip() for token in tokens if token.strip()]

        ids = [
            self.str_to_int.get(token, self.str_to_int["<|unk|>"])
            for token in tokens
        ]

        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.!?;:"()\'"])', r'\1', text)
        return text