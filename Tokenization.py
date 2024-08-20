import torch
import math

"""
Tokenization - Using the Byte Pairing Encoding Algorithm. Train a Tokenizer based on the Epictetus Dataset.
"""

class BPETokenizer:

    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.utf8_vocab = {idx: bytes([idx]) for idx in range(256)}
        self.tokens = None


    def encode(self):
        # Load as byte data:
        tokens = self.raw_text.encode("utf-8")
        tokens = [int(token) for token in tokens]
        self.tokens = tokens
        pass
    def tokenize(self):
        pass

    def decode(self):
        text = ''.join(self.utf8_vocab[token].decode('utf-8') for token in self.tokens)
        print(text)
        pass


if __name__ == '__main__':
    # Test Loop:
    tokenizer = BPETokenizer('This is a sentence.')
    tokenizer.encode()
    tokenizer.decode()