import torch
from torch.autograd import Variable
from torch import nn, autograd, optim

class CharBasedRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, n_layers,lang):
        super(CharBasedRNN, self).__init__()
        self.lang=lang
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.n_layers = n_layers

        self.embedding = nn.Embedding(input_size, 300)
        self.embedding.weight = nn.Parameter(torch.FloatTensor(self.lang.vec))
        self.lstm = nn.LSTM(300, hidden_size, n_layers, bidirectional=True)
        self.out = nn.Linear(hidden_size * 2, output_size)

    def forward(self, char_input, hidden):
        seq_len = len(char_input)
        embedded = self.embedding(char_input).view(seq_len, 1, -1)

        # print concat_input
        output, hidden = self.lstm(embedded, hidden)
        output = self.out(output.view(1, -1))
        return output, hidden

    def init_hidden(self):
        return (Variable(torch.zeros(self.n_layers * 2, 1, self.hidden_size)),
                Variable(torch.zeros(self.n_layers * 2, 1, self.hidden_size)))


