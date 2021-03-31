import pickle

from lyrics_prediction.song_prediction import SongGenerator
from lyrics_prediction.build_model import RNNTools

from corpus_blender.corpus_blender import CorpusBlender

rnn_tool = RNNTools()

# Load model
# Model file can be downloaded from here:
# pickle: https://drive.google.com/file/d/1BgHvAuTm8nPOSLzDydX_uPfY3OATUBhF/view?usp=sharing
# model: https://drive.google.com/file/d/1T0SScM4xkNzWQrje1gxtiF8ez0AMHzqi/view?usp=sharing

cp = '70000'
with open(f"./model/lang.checkpoint.{cp}", "rb") as output_file:
    lang = pickle.load(output_file)
    rnn_tool.load_model(lang=lang)


def start():
    s = SongGenerator()
    s.rnnTool = rnn_tool
    cb = CorpusBlender(s)
    cb.create_song()
    s.print_songs()


if __name__ == '__main__':
    start()
