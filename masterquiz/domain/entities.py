class Question:
    def __init__(self, id, text, a, b, c, correct, difficulty):
        self.__id=id
        self.__text=text
        self.__a=a
        self.__b=b
        self.__c=c
        self.__correct=correct
        self.__difficulty=difficulty

    def get_id(self):
        return self.__id

    def get_text(self):
        return self.__text

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_correct(self):
        return self.__correct

    def get_difficulty(self):
        return self.__difficulty

    def __str__(self):
        return "Id:{0}, Text:{1}, Answers: {2}, {3}," \
               " {4}, Correct: {5}, Difficulty:{6}".format(self.get_id(), self.get_text(), self.get_a(),
                                                           self.get_b(), self.get_c(), self.get_correct(),
                                                           self.get_difficulty())

    def __eq__(self, other):
        return self.__id == other.get_id()


class Quiz:
    def __init__(self, difficulty, nr, file_name):
        self.__difficulty = difficulty
        self.__nr = nr
        self.__file_name = file_name
        #self.__questions=[]

    def get_difficulty(self):
        return self.__difficulty
    
    def get_nr(self):
        return self.__nr

    def get_file_name(self):
        return self.__file_name

