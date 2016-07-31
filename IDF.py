from __future__ import division
from stop_words import get_stop_words
import string

class IDF:
    def __init__(self, str_1, str_2, corpus):
        self.corpus = corpus

        # remove punctuation
        str_1 = str_1.translate(string.maketrans("", ""), string.punctuation)
        str_2 = str_2.translate(string.maketrans("", ""), string.punctuation)

        # Tokenize the sentence
        self.str_1 = self.tokenize(str_1)
        self.str_2 = self.tokenize(str_2)

    # tokenize str and remove stop words
    def tokenize(self, item):
        item = item.lower().split(" ")
        for token in item:
            if token in self.stop_words:
                item.remove(token)
        return item