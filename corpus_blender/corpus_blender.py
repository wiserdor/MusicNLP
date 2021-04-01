from nltk.corpus import gutenberg  # brown, comparative_sentences, sentence_polarity
import nltk
import random

# Download corpus
# nltk.download('brown')
# nltk.download('comparative_sentences')
# nltk.download('sentence_polarity')
nltk.download('gutenberg')

num_of_sents_to_predict = 15000  # the grater the number, the grater the odds and the longer it takes to predict
max_sentence_length = 2


class CorpusBlender:
    def __init__(self, song_generator=None):
        self.song_generator = song_generator

        # Can be any list of sentences
        self.sents_list = gutenberg.sents(
            ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt'])

    def create_song(self):
        print('Creating songs')
        corpus_for_prediction = ''

        for i in range(num_of_sents_to_predict):
            sent_chosen = random.choice(self.sents_list)
            corpus_for_prediction += ' '.join(sent_chosen)

        self.song_generator.predict(corpus_for_prediction)
