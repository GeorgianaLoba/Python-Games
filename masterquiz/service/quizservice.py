from domain.entities import Quiz, Question


class QuizService:
    def __init__(self, quiz_repo, question_serv):
        self.__quiz_repo = quiz_repo
        self.__question_serv = question_serv

    def create_quiz(self, difficulty, nr, file_name):
        """
        First the function opens a file with the given file_name and writes to that file
        questions that have the given difficulty; we constantly check if the condition given is met and also
        using a counter parameter, we count how many questions we write into the file(we need to write
        'nr' questions.
        Afterwards, we create a quiz with the given parameters
        :param difficulty:
        :param nr:
        :param file_name:
        """
        f = open(file_name, 'w+')
        questions = self.__question_serv.get_all_questions()
        counter = 0
        for question in questions:
            if str(question.get_difficulty()) == str(difficulty):
                if counter<=int(nr):
                    f.writelines(str(question.get_id()) + ";" + str(question.get_text()) + ";" +
                                 str(question.get_a()) + ";" + str(question.get_b()) + ";" +
                                 str(question.get_c()) + ";" + str(question.get_correct()) + ";"
                                 + str(question.get_difficulty()) + "\n")
                counter += 1
        if counter >= int(nr) // 2:
            for question in questions:
                if counter<int(nr):
                    if question.get_difficulty() == difficulty:
                        pass
                    else:
                        if counter > int(nr):
                            f.write(str(question.get_id()) + ";" + str(question.get_text()) + ";" +
                                    str(question.get_a()) + ";" + str(question.get_b()) + ";" +
                                    str(question.get_c()) + ";" + str(question.get_correct()) + ";" +
                                    str(question.get_difficulty()) + "\n")
                    counter += 1
        else:
            raise Exception("not enough questions of that difficulty")
        f.close()
        self.__quiz_repo.add(Quiz(difficulty, nr, file_name))

    def get_questions_from_quiz_file(self, file_name):
        """
        Returns a list of questions from a certain quiz file.
        """
        questions=[]
        with open(file_name, 'r') as f:
            for line in f:
                l = line.split(';')
                l[6] = l[6].split('\n')
                questions.append(Question(l[0], l[1], l[2], l[3], l[4], l[5], l[6][0]))
        return list(questions)

    def start_game(self, file_name):
        """
        Checks if the quiz given by the user exist and if so, returns the questions from the quiz
        """
        quizez = self.__quiz_repo.get_all()
        if file_name in quizez:
            questions=self.get_questions_from_quiz_file(file_name)
            return questions
        else:
            raise Exception("the quiz doesn't exist")

    def get_all_quizez(self):
        return self.__quiz_repo.get_all()