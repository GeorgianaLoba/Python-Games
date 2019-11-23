from domain.entities import Question


class QuestionRepo:
    def __init__(self, file_name):
        #self.__master_quiz=[]
        self.__questions=[]
        self.__file_name=file_name
        self.read_from_file()

    def get_all(self):
        return self.__questions[:]

    def len(self):
        return len(self.__questions)
    def add(self, question):
        if question in self.__questions:
            raise Exception('already exists')
        self.__questions.append(question)

    def read_from_file(self):
        with open(self.__file_name, 'r') as f:
            for line in f:
                l=line.split(';')
                l[6]=l[6].split('\n')
                self.__questions.append(Question(l[0], l[1], l[2], l[3], l[4], l[5], l[6][0]))