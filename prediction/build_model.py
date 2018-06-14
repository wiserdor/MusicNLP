import numpy as np
import os
from prediction.word_rnn import CharBasedRNN
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import random
import csv
import pickle
import time
import re
import sys

MAX_SEQ_LEN = 69


class RNNTools:
    def __init__(self):
        self.lang=None
        self.model=None


    """Neaural network functionality"""

    """model utilities"""

    def softmax(self,x):
        return np.exp(x) / np.sum(np.exp(x), axis=0)

    def precision(self,output, target):
        true_pos = 0
        false_pos = 0
        for i in range(len(output)):
            if output[i] == 1:
                if target[i] == 1:
                    true_pos += 1
                else:
                    false_pos += 1

        return true_pos / (true_pos + false_pos)

    def recall(self,output, target):
        true_pos = 0
        overall = 0
        for i in range(len(output)):
            if output[i] == 1:
                if target[i] == 1:
                    true_pos += 1
            if output[i] == 0:
                if target[i] == 1:
                    overall += 1
        return true_pos / (true_pos + overall)


    def sentence2variable(self,input_vec, output):
        input_var = Variable(torch.LongTensor(input_vec).view(-1, 1))
        target_var = Variable(torch.LongTensor(output).view(-1, 1))
        return (input_var, target_var)


    def format_text(self,text):
        new_word_list = []
        for word in text.split():
            if (word == " "):
                continue
            word = re.sub(r"[^A-Za-z0-9:.<>/]", "", word.strip())
            new_word_list += word.split()

        cleaned_text = []
        for word in range(0, len(new_word_list)):
            cleanr = re.compile('<.*?>')
            cleaned_text.append(re.sub(cleanr, '', new_word_list[word]))
            if (cleaned_text[-1].endswith('.')):
                while (cleaned_text[-1].endswith('.')):
                    cleaned_text[-1] = cleaned_text[-1][:-1]
                cleaned_text.append('.')
        return cleaned_text




    def load_file(self,filepath):
        with open(filepath) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            text = next(csvReader)
            try:
                tags = next(csvReader)
                while (len(tags) == 0):
                    tags = next(csvReader)
            except:
                tags = [0] * len(text)
            dot_count = 0
            for s in range(len(text) - 1, 0, -1):
                if tags[s] not in ('0', '1'):
                    tags[s] = '0'
                if text[s] == '.':
                    dot_count += 1
                else:
                    dot_count = 0
                if dot_count > 1:
                    del text[s + 1]
                    del tags[s + 1]
            output_vec = []
            input_vec = []
            for i in range(0, len(text)):
                input_vec.append(self.lang.get_token_id(text[i]))
                output_vec.append(int(tags[i]))

            # building instances
            instances = []
            instance_input = []
            instance_output = []
            for i in range(0, len(input_vec)):
                instance_input.append(input_vec[i])
                instance_output.append(output_vec[i])
                if self.lang.ind2word[input_vec[i]] == "." or i == len(input_vec) - 1 or len(instance_input) >= MAX_SEQ_LEN:
                    instances.append(self.sentence2variable(instance_input, instance_output))
                    instance_input = []
                    instance_output = []

            return instances


    def load_text(self,text):
        text = self.format_text(text);
        tags = [0] * len(text)
        dot_count = 0
        for s in range(len(text) - 1, 0, -1):
            if tags[s] not in ('0', '1'):
                tags[s] = '0'
            if text[s] == '.':
                dot_count += 1
            else:
                dot_count = 0
            if dot_count > 1:
                del text[s + 1]
                del tags[s + 1]

        output_vec = []
        input_vec = []
        for i in range(0, len(text)):
            input_vec.append(self.lang.get_token_id(text[i]))
            output_vec.append(int(tags[i]))

        # building instances
        instances = []
        instance_input = []
        instance_output = []
        for i in range(0, len(input_vec)):
            instance_input.append(input_vec[i])
            instance_output.append(output_vec[i])
            if self.lang.ind2word[input_vec[i]] == "." or i == len(input_vec) - 1 or len(instance_input) >= MAX_SEQ_LEN:
                instances.append(self.sentence2variable(instance_input, instance_output))
                instance_input = []
                instance_output = []

        return instances


    def build_dataset_csv(self,*args):
        data = []
        for f in args[0]:
            print(f)
            if not f.endswith('.csv'):
                continue

            print("processing", f)
            instances = self.load_file(f)
            for i in instances:
                data.append(i)
        return data


    def build_dataset_text(self,text):
        data = []
        instances = self.load_text(text)
        for i in instances:
            data.append(i)
        return data

