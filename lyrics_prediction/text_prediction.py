from lyrics_prediction.build_model import *


class PredictText:
    def __init__(self):
        self.model_init()
        self.rnnTool = None

        self.data = None
        self.model_ready = True
        self.text_loaded = False
        self.text_predicted = False
        self.save_path = './text_predictions/'

    def model_init(self):
        self.seq_input = ""
        self.naked_text = []
        self.seq_output = [1]
        self.seq_target = [1]

    def save_predicted_text_to_txt(self, file_name=None):
        if not os.isdir(save_path):
            os.mkdir(save_path)
        if not txt_name:
            txt_name = time.now()

        text_file = open(self.save_path + file_name, "w")
        text_file.write(self.get_predicted_text())
        text_file.close()

    def predict_csv(self, *args):
        self.data = self.rnnTool.build_dataset_csv(args)
        self.predict()

    def predict(self, raw_text=None):
        self.model_init()
        # TODO: check if text>wanted text size
        if raw_text:
            self.data = self.rnnTool.build_dataset_text(raw_text)
        if self.data:
            self.model_ready = False
            for i in self.data:
                hidden = self.rnnTool.model.init_hidden()
                self.seq_target.extend([item for sublist in i[1].data.numpy() for item in sublist])

                for j in i[0]:
                    seq_len = len(j.data)
                    for o in range(seq_len):
                        output_tag_id = 1
                        try:
                            output, hidden = self.rnnTool.model(j[o], hidden)
                            output_tag_id = np.argmax(self.rnnTool.softmax(output.data.numpy()[0]))
                            if (self.rnnTool.lang.ind2word[j[o].data.numpy()[0]] == '.'):
                                output_tag_id = self.seq_output[-1]

                            print("Word:", self.rnnTool.lang.ind2word[j[o].data.numpy()[0]])
                            print("Prediction:", output_tag_id)

                        except:
                            output_tag_id = self.seq_output[-1]
                            print("Word:", self.rnnTool.lang.ind2word[j[o].data.numpy()[0]])
                            print("Prediction:", output_tag_id)

                        if (output_tag_id == 1):
                            self.seq_input += " \033[1m" + self.rnnTool.lang.ind2word[j[o].data.numpy()[0]] + '\033[0m'
                        else:
                            self.seq_input += " " + self.rnnTool.lang.ind2word[j[o].data.numpy()[0]]

                        self.seq_output.append(output_tag_id)
                        self.naked_text.append(self.rnnTool.lang.ind2word[j[o].data.numpy()[0]])
            del (self.seq_output[0])
            del (self.seq_target[0])
            self.smooth_ones()
            self.smooth_zeros()
            self.model_ready = True
            self.text_predicted = True

    def smooth_ones(self, gap=17):
        so1 = self.seq_output[:]
        counter = 0
        sindex = 0
        dotindex = 0
        for i in range(len(so1)):
            if (self.naked_text[i] == '.'):
                dotindex = i
            if (so1[i] == 1):
                if (counter < gap and counter > 0):
                    for j in range(min(dotindex, sindex), i):
                        so1[j] = 1
                sindex = i
                counter = 0
            else:
                counter += 1
        self.seq_output = so1

    def smooth_zeros(self, gap=90):
        so1 = self.seq_output[:]
        counter = 0
        dotindex = 0
        sindex = 0

        for i in range(len(so1)):
            if (self.naked_text[i] == '.'):
                dotindex = i
            if (so1[i] == 0):
                if (counter < gap and counter > 0):
                    for j in range(min(dotindex, sindex), i):
                        so1[j] = 0
                sindex = i
                counter = 0
            else:
                counter += 1
        self.seq_output = so1

    def __str__(self):
        if self.text_predicted:
            last1 = ""
            for i in range(len(self.naked_text)):
                if self.seq_output[i] == 1:
                    last1 += " \033[1m" + self.naked_text[i] + '\033[0m'
                else:
                    last1 += " " + self.naked_text[i]
            return last1
        else:
            print('error: no text predicted yet')
            return ''
