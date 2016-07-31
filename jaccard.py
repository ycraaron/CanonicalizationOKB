from __future__ import division
from stop_words import get_stop_words
import string

class Jaccard:

    def __init__(self, str_1, str_2):
        self.stop_words = get_stop_words('en')

        # Remove punctuations
        str_1 = str_1.translate(string.maketrans("", ""), string.punctuation)
        str_2 = str_2.translate(string.maketrans("", ""), string.punctuation)

        # Tokenize the sentence
        self.str_1 = self.tokenize(str_1)
        self.str_2 = self.tokenize(str_2)

    # cal intersect
    def intersect(self):
        return [i for i in self.str_1 if i in self.str_2]

    # cal union
    def union(self):
        return set(self.str_1 + self.str_2)

    # cal similarity
    def similarity(self):
        intersect = len(self.intersect())
        union = len(self.union())
        if intersect == None and union == None:
            return 1
        return intersect / union

    # cal distance
    def distance(self):
        return 1 - self.similarity()

    # tokenize str and remove stop words
    def tokenize(self, item):
        item = item.lower().split(" ")
        for token in item:
            if token in self.stop_words:
                item.remove(token)
        return item

jaccard = Jaccard("Aaron", "Aaron, is a awesome genius")

similarity = jaccard.similarity()
distance = jaccard.distance()

print similarity
print distance