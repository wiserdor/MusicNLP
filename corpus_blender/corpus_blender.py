from nltk.corpus import brown, comparative_sentences, sentence_polarity
import nltk
import random

# Download corpus
nltk.download('brown')
nltk.download('comparative_sentences')
nltk.download('sentence_polarity')


max_search_length = 50
min_search_length = 20


class CorpusBlender:
    def __init__(self, song_generator=None):
        self.song_generator = song_generator
        self.corpuses_list = [brown, comparative_sentences, sentence_polarity]

    def create_song(self):
        print('Creating songs')
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
