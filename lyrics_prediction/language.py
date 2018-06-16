"""Class that holds word vectors with glove word embedding"""


class Lang:
    def __init__(self):
        # self.vocab = {}
        self.vec = []
        self.word_count = 0
        self.ind2word = {}
        self.word2ind = {}
        for line in open("./lyrics_prediction/model/glove.6B.300d.txt", encoding="utf8"):
            values = line.split(" ")
            v = []
            for i in range(1, len(values)):
                v.append(float(values[i]))
            self.vec.append(v)
            self.ind2word[self.word_count] = values[0]
            self.word2ind[values[0]] = self.word_count
            self.word_count += 1

    def get_token_id(self, token):
        if token not in self.word2ind:
            self.word2ind[token] = self.word_count
            self.vec.append([0] * 300)
            self.ind2word[self.word_count] = token
            self.word_count += 1
        return self.word2ind[token]
