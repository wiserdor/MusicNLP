from nltk.corpus import brown, twitter_samples, comparative_sentences, shakespeare, nps_chat, sentence_polarity
import random
from lyrics_prediction.song_prediction import SongGenerator

max_search_length = 500
min_search_length = 100


class CorpusBlender:
    def __init__(self, song_generator=None):
        self.song_generator = song_generator
        self.corpuses_list = [brown, comparative_sentences, sentence_polarity]

    def create_song(self):

        sentences_num = random.randrange(min_search_length, max_search_length)
        corpus_sentences_num = random.randrange(0, sentences_num)
        rand_sentences = []

        for i in range(corpus_sentences_num):
            corpus_num = random.randrange(0, len(self.corpuses_list))
            if corpus_num == 1:
                sentence_num = random.randrange(0, len(self.corpuses_list[corpus_num].comparisons()))
                rand_sentences.append(self.corpuses_list[corpus_num].comparisons()[sentence_num].text)
            else:
                sentence_num = random.randrange(0, len(self.corpuses_list[corpus_num].sents()))
                rand_sentences.append(self.corpuses_list[corpus_num].sents()[sentence_num])

        corpus_for_prediction = ''
        for sentence in rand_sentences:
            corpus_for_prediction += ' '.join(sentence)
        self.song_generator.predict(corpus_for_prediction)
