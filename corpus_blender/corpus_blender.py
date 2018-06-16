from nltk.corpus import brown, sentence_polarity
import random
from lyrics_prediction.song_prediction import SongGenerator

max_search_length = 20
min_search_length = 10


class CorpusBlender:
    def __init__(self, song_generator=None):
        self.song_generator = song_generator

    def create_song(self):

        sentences_num = random.randrange(min_search_length, max_search_length)
        polarity_sentences_num = random.randrange(0, sentences_num)
        corpus_sentences_num = sentences_num - polarity_sentences_num
        rand_polar_sentences = []
        polarity_type = sentence_polarity.categories()[random.randrange(0, 1)]
        for i in range(polarity_sentences_num):
            rand_polar_sentences.append(sentence_polarity.sents(categories=polarity_type)[random.randrange(0, len(
                sentence_polarity.sents(categories=polarity_type)))])

        rand_corpus_sentences = []
        for i in range(corpus_sentences_num):
            rand_corpus_sentences.append(brown.sents()[random.randrange(0, len(brown.sents()))])
        corpus_for_prediction = ''
        for sentence in rand_polar_sentences:
            corpus_for_prediction += ' '.join(sentence)
        for sentence in rand_corpus_sentences:
            corpus_for_prediction += ' '.join(sentence)
        print(corpus_for_prediction)
        self.song_generator.predict(corpus_for_prediction)
