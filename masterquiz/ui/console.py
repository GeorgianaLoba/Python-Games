class Console:
    def __init__(self, question_serv, quiz_serv):
        self.__question_serv = question_serv
        self.__quiz_serv = quiz_serv

    def ui_print(self, list=None):
        """
        Prints the existing questions and quizes
        """
        questions=self.__question_serv.get_all_questions()
        for question in questions:
            print(question)
        quizez = self.__quiz_serv.get_all_quizez()
        for quiz in quizez:
            print(quiz)

    def ui_start(self, list):
        """
        Starts the game, in questions we will receive all the questions from the specific quiz.
        Points will store the points gained from correct answers.
        We print and count the points of the question one by one
        """
        questions=self.__quiz_serv.start_game(list[0])
        points=0
        for question in questions:
            print('\n'+question.get_text()+"\n"+question.get_a()+"\n"+question.get_b()+'\n'+question.get_c()+'\n')
            answer = input("Pick your answer: ")
            answer.strip()
            #check correct is a functions that returns either 0(wrong answer), 1(easy correct answer)...
            points += self.__question_serv.check_correct(question, answer)
        print("You have a total of " + str(points)+" points")

    def ui_create(self, list):
        #creates a new quiz
        try:
            self.__quiz_serv.create_quiz(list[0], list[1], list[2])
        except:
            raise Exception("wrong format")

    def ui_add(self, list):
        #adds a new question to my list and file of questions
        try:
            self.__question_serv.add_question(list[0], list[1], list[2], list[3], list[4], list[5], list[6])
        except:
            raise Exception("wrong format")

    def read_cmd(self):
        """
        Reads input from the user and splits it accordingly since we have a specific format
        :return: command and a list(of variables)
        """
        line=input("Enter your command: ")
        space=line.find(' ')
        if space==-1:
            return line, [] #in the case of print, we only have the command, therefore, we return an empty list
        else:
            cmd=line[:space]
            args=line[space+1:]
            args=[s.strip() for s in args.split(';')]
            return cmd, args

    def display(self):
        print('\nHello\n'
              'This is a program that allows creating and solving quizzez!\n'
              'You are able to do the following:\n'
              'ADD a question using the command: add <id>; <text>; <choice_a>; <choice_b>; <choice_c>; <correct_choice>; <difficulty>\n'
              'CREATE a new quiz using the command: create <difficulty> <number of questions> <file_name>\n'
              'Play a quiz using: start <file_name>\n'
              'Check again the available commands typing the command: show\n'
              'Print everything using: print\n'
              'Exit by typing the command: exit\n')

    def show_commands(self, list=None):
        print('\nADD a question using the command: add <id>; <text>; <choice_a>; <choice_b>; <choice_c>; <correct_choice>; <difficulty>\n'
              'CREATE a new quiz using the command: create <difficulty> <number of questions> <file_name>\n'
              'PLAY a quiz using: start <file_name>\n'
              'Check again the available commands typing the command: show\n'
              'Print everything using: print\n'
              'Exit by typing the command: exit\n')

    def menu(self):
        #the available commands are stored in a dictionary
        self.display()
        commands={'add':self.ui_add,
                  'create':self.ui_create,
                  'start': self.ui_start,
                  'show': self.show_commands,
                  'print':self.ui_print
                  }
        while True:
            cmd, args=self.read_cmd()
            if cmd == 'exit':
                print('seeya')
                break
            try:
                commands[cmd](args)
            except Exception as ex:
                print(ex)



