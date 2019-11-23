from domain.entities import Question


class QuestionServ:
    def __init__(self, question_repo):
        self.__question_repo = question_repo

    def get_all_questions(self):
        #returns all questions
        return self.__question_repo.get_all()

    def create_question(self, code, text, a, b, c, correct, diff):
        #create an instance of class question
        question = Question(code, text, a, b, c, correct, diff)
        return question

    def add_question(self, code, text, a, b, c, correct, diff):
        #adds a question to my list of questions
        self.__question_repo.add(self.create_question(code, text, a, b, c, correct, diff))

    def check_correct(self, question, answer):
        #check the correctness of an answer and returns points according to difficulty
        if question.get_correct()==answer:
            if question.get_difficulty()=='easy':
                return 1
            elif question.get_difficulty()=='medium':
                return 2
            else:
                return 3
        else:
            return 0