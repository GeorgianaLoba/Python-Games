from hangman.domain.entities import Sentence

class Sentences:
    def __init__(self, file_name):
        self.__sentences = []
        self.__file_name = file_name
        self.read_from_file()

    def get_all(self):
        return self.__sentences[:]

    def add(self, sentence):
        self.__sentences.append(Sentence(sentence))
        self.write_to_file(sentence)

    def write_to_file(self, sentence):
        with open(self.__file_name, 'a') as f:
            f.write('\n')
            f.write(sentence)

    def read_from_file(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                l=line.split('\n')
                self.__sentences.append(Sentence(l[0]))

