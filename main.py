import pickle
from prediction.song_generator import SongGenerator
import torch.nn.functional as F
import torch
from prediction.build_model import RNNTools
from prediction.language import Lang
from prediction.word_rnn import CharBasedRNN

"""setup"""

rnntool=RNNTools()
cp = "70000"
with open(r"./prediction/model/lang.checkpoint." + cp, "rb") as output_file:
    rnntool.lang = pickle.load(output_file)
hidden_size = 500
n_layers = 1
n_tags = 2
rnntool.model = CharBasedRNN(rnntool.lang.word_count, hidden_size, n_tags, n_layers, rnntool.lang)
rnntool.model.load_state_dict(
    torch.load("./prediction/model/model.checkpoint." + cp, map_location=lambda storage, loc: storage))
rnntool.model.cpu()
rnntool.model.eval()

s=SongGenerator()
s.rnnTool=rnntool
s.predict('hello is it me you. looking for i can see it. in your eyes')




