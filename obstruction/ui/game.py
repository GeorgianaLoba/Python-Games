from sys import exit

from players.computer import Computer
from players.human import Human


class Game:
    #TODO: look for a weird print
    def __init__(self, p1, p2, board, minimax):
        self.__p1 = p1
        self.__p2 = p2
        self.board = board
        self.minimax = minimax
        self.__last_move = None
        self.count = 0 #count is used for the minimax algotithm

    def start(self):
        while True:
            try:
                while True: #we make moves until the game is over, starting with the human('x) and after, the comp('0')
                    self.__move(self.__p1, 'x')
                    self.count +=1
                    if self.__last_move.get_value() == 'x': #computer makes a move only if the player already made one
                        self.__move(self.__p2, '0')
                        self.count += 1
            except ValueError as ve:
              print(ve)
            except Exception as ex:
                print(ex)

    def __move(self, player, value):
        if len(self.board.get_empty_cells()) != 0:
            line, column = -1, -1
            if type(player) is Human: # if the player is human, we draw the board and then read data from user
                self.__draw_board()
                line, column = self.__read_data()
            if type(player) == Computer and self.count>4: #this is for the minimax algorithm
                #thats starts when we already have 4 moves on the board
                line, column = self.minimax.minimax(self.board)
            lst = player.move(line, column, value) #the actual move is made here
            #the move function will return a list that contains a cell, that cell line and column and then, a list
            #of lists containing each the line and column of the surrounding cells
            self.__last_move = lst[0]  #we save in last_move the last move made which is a cell object
            game_status, winner_value = self.__is_over() #check the game status
            if game_status is True:
                self.__game_over(winner_value)

    def __is_over(self):
        """
        This function checks if the board no longer has empty cells, if so, it returns true and the value
        of the last player who made a move (the winner)
        """
        value = self.__last_move.get_value()
        if len(self.board.get_empty_cells()) == 0:
            return True, value
        return False, value

    def __game_over(self, winner_value):
        """
        Checks if either the player or the computer won and prints messages accordingly.
        Also exits the game.
        """
        print("Game over!")
        self.__draw_board()
        if winner_value == 'x':
            print("You won! Good job!")
        else:
            print("Computer wins, you loser.")
            exit()

    def __draw_board(self):
        print(self.board)

    def __read_data(self):
        """
            This will read the data from the user. It is required to numbers that are split
            by space. The function return as the parameters 2 float numbers.
        """
        line = input("Enter your choice (line, column separated by space)."
                     "Initialization is 1: ")
        l = line.split(' ')
        try:
            index1 = float(l[0])
            index2 = float(l[1])
            return index1-1, index2-1 #-1 is due to the fact that in the actual board, we start indexing by 0
        except:
            raise ValueError("You need to enter an int.")