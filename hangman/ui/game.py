class Game:
    def __init__(self, service):
        self.__service = service

    def __ui_add(self):
        line = input("Enter your sentence. Be imaginative: \n")
        self.__service.add_sentence(line.strip())

    def __ui_start(self):
        #gets a random sentence, save a copy of it
        hangman="hangman"
        over=""
        counter=0
        sentence = self.__service.get_one()
        final_sentence=sentence[:]
        chars=[]
        new_sentence, chars=self.__service.make_initial_hangman(sentence)

        while True:
            print(new_sentence+" - "+over)
            letter = input("Enter a letter: ")

            if self.__service.check_letter(letter, final_sentence):
                chars.append(letter)
                new = ""
                for char in final_sentence:
                    if char in chars:
                        new+=char
                    elif char==" ":
                        new+=" "
                    else:
                        new+="_"
                new_sentence=new[:]
                if new_sentence==final_sentence:
                    print("You won.congrats")
                    self.menu()
            else:
                counter+=1
                over=hangman[:counter]
                if over == hangman:
                    print("GAME OVER! You loser...")
                    self.menu()

    def __ui_print(self):
        sentences = self.__service.get_all_sentences()
        for sentence in sentences:
            print(sentence)

    def display(self):
        print("Hello\n"
              "This is a hangam game in which you can do the following:\n"
              "Add a sentence by typing 1\n"
              "Start a new game by typing 2\n"
              "Print all sentences by typing 3\n")

    def menu(self):
        self.display()
        try:
            while True:
                try:
                    choice = int(input("Enter your choice: "))
                except:
                    raise Exception("need int")
                if choice==0:
                    print('seeya')
                    break
                if choice==1:
                    self.__ui_add()
                if choice==2:
                    self.__ui_start()
                if choice==3:
                    self.__ui_print()
        except Exception as ex:
            print(ex)
