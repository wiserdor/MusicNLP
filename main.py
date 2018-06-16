import pickle
from lyrics_prediction.song_prediction import SongGenerator
from lyrics_prediction.build_model import RNNTools
from lyrics_prediction.language import Lang
from lyrics_prediction.word_rnn import CharBasedRNN
from corpus_blender.corpus_blender import CorpusBlender

"""setup"""

rnntool = RNNTools()
cp = '70000'
with open(r"./lyrics_prediction/model/lang.checkpoint." + cp, "rb") as output_file:
    lang = pickle.load(output_file)
    rnntool.load_model(lang=lang)

s = SongGenerator()
s.rnnTool = rnntool
cb = CorpusBlender(s)
cb.create_song()
s.print_songs()
