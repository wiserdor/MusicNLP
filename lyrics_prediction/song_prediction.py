from lyrics_prediction.text_prediction import PredictText


class SongGenerator(PredictText):
    def __init__(self):
        super().__init__()
        self.songs_list = [[]]
        self.num_of_songs = 0

    def generate_songs_list(self):
        co = 0
        self.num_of_songs = 0
        self.songs_list = [[]]
        for i in range(len(self.naked_text)):
            if self.naked_text[i] == ' ' or self.naked_text[i] == '':
                continue
            last1 = self.naked_text[i] + ' '
            print(last1)
            if self.seq_output[i] == 1:
                if co == 0:
                    print("song number:", self.num_of_songs + 1, "\n")
                else:
                    self.songs_list[self.num_of_songs].append(last1)
                co += 1

            else:
                if co > 0:
                    self.num_of_songs += 1
                    self.songs_list.append([])
                co = 0
        return self.songs_list

    def print_songs(self):
        print('Total songs:', len(self.num_of_songs))
        all_songs = ''
        for song in range(len(self.songs_list)):
            all_songs += str('song number:' + str(song + 1) + '\n')
            for word in self.songs_list[song]:
                all_songs += word + ' '
            all_songs += '\n'
        print(all_songs)

    def predict(self, raw_text=None):
        super().predict(raw_text)
        self.generate_songs_list()
