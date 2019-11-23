import random

from hangman.domain.entities import Sentence


class Service:
    def __init__(self, sentences):
        self.__sentences=sentences

    def check_validity(self, line):
        words=line.split(' ')
        counter=0
        for word in words:
            counter+=1
            c=0
            for character in word:
                c+=1
            if c<3:
                return False
        if counter<1:
            return False
        return True

    def check_letter(self, letter, sentence):
        for char in sentence:
            if char==letter:
                return True
        return False

    def make_initial_hangman(self, sentence):
        characters=[]
        words=sentence.split(' ')
        for word in words:
            characters.append(word[0])
            characters.append(word[-1])
        new_sentence =""
        for char in sentence:
            if char in characters:
                new_sentence+=char
            elif char==' ':
                new_sentence+=' '
            else:
                new_sentence+='_'
        return new_sentence, characters

    def get_one(self):
        sentences=self.__sentences.get_all()
        return random.choice(sentences).get_line()

    def check_exists(self, line):
        sentences = self.__sentences.get_all()
        for sentence in sentences:
            if sentence == line:
                return False
        return True

    def get_all_sentences(self):
        return self.__sentences.get_all()

    def add_sentence(self, line):
        if self.check_validity(line):
            if self.check_exists(Sentence(line)):
                self.__sentences.add(line)
            else:
                raise Exception("already exists")
        else:
            raise Exception('wrong format of sentence, try again')