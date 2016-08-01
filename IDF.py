from __future__ import division
from stop_words import get_stop_words
import string
import math
import operator

class IDF:
    def __init__(self, str_1, str_2, corpus):
        self.list_corpus = corpus
        self.stop_words = get_stop_words('en')
        # remove punctuation
        str_1 = str_1.translate(string.maketrans("", ""), string.punctuation)
        str_2 = str_2.translate(string.maketrans("", ""), string.punctuation)
        #self.list_corpus = []
        # Tokenize the sentence
        self.str_1 = self.tokenize(str_1)
        self.str_2 = self.tokenize(str_2)
        #print "st1",str_1,"st2",str_2
        #print "cccc",corpus
        # for i in range(len(corpus)):
        #     item = str(corpus[i]).split(" ")
        #     for token in item:
        #         if token in self.stop_words:
        #             pass
        #         else:
        #             self.list_corpus.append(token)

    def intersect(self):
        return [i for i in self.str_1 if i in self.str_2]

    def union(self):
        return list(self.str_1 + self.str_2)

    # tokenize str and remove stop words
    def tokenize(self, item):
        item = item.split(" ")
        for token in item:
            if token in self.stop_words:
                item.remove(token)
        return item

    def cal_overlap(self):
        list_intersect = self.intersect()
        list_union = self.union()
        freq_inter = 0.0
        freq_union = 0.0
        for item in list_intersect:
            matches_intersect = [x for x in self.list_corpus if item == x]
            freq_inter += math.log10(operator.pow(len(matches_intersect) + 1, -1))

        for item in list_union:
            if len(list_union)==0:
                print self.str_1,self.str_2
            matches_union = [x for x in self.list_corpus if item == x]
            freq_union += math.log10(operator.pow(len(matches_union) + 1, -1))
        #print "cor", self.list_corpus
        #print list_intersect,list_union
        idf_overlap = freq_inter / freq_union
        return idf_overlap
        # print matches_intersect, freq_inter
        # print matches_union, freq_union
        #
        # print "intersect", list_intersect
        # print "union", list_union
        # print "corpus", self.list_corpus