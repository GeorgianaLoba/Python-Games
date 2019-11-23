class QuizRepo:
    def __init__(self, file_name):
        self.__quiz=[] #will store every quiz's name
        self.__file_name=file_name
        self.read_from_file()


    def len(self):
        return len(self.__quiz)

    def add(self, quiz):
        """
        Adds a quiz name to my list of quizez
        :param quiz:
        :return:
        """
        if quiz.get_file_name() not in self.__quiz:
            self.__quiz.append(quiz.get_file_name())
            self.write_to_file(quiz)
        else:
            raise Exception

    def read_from_file(self):
        """
        Reads from a file the already existing quizez names
        """
        with open(self.__file_name, 'r') as f:
            for line in f:
                l=line.split('\n')
                self.__quiz.append(l[0])

    def write_to_file(self, quiz):
        """
        writes to a file quizes' names
        """
        with open(self.__file_name, 'a') as f:
            f.write('\n')
            f.write(quiz.get_file_name())

    def get_all(self):
        return self.__quiz[:]