import tkinter

from board.board import Board
from board.gui_board import GuiBoard
from gui.gui import Gui
from gui.gui_game import GuiGame
from players.computer import Computer
from players.gui_human import GuiHuman
from players.human import Human
from strategy.minimax import Minimax
from strategy.nostrategy import NoStrategy
from strategy.strategy import Strategy
from ui.game import Game


def main():
    "Crates a window with a label and three buttons"
    window = tkinter.Tk()
    window.title("Menu")
    label = tkinter.Label(window, text="HELLO")
    label.grid()
    button1 = tkinter.Button(window, text="START WITH UI", command=start_ui)
    button1.grid()
    button2 = tkinter.Button(window, text="Start with GUI", command=start_gui)
    button2.grid()
    button3 = tkinter.Button(window, text="EXIT", command = exit)
    button3.grid()
    window.mainloop()

def start_ui():
    board = Board(6, 6)
    strategy = Strategy()
    p1 = Human('x', board)
    p2 = Computer("0", board, strategy)
    minimax = Minimax()
    game = Game(p1, p2, board, minimax)
    game.start()

def start_gui():
    board = GuiBoard(9, 9)
    strategy = Strategy()
    p1 = GuiHuman('x', board)
    p2 = Computer('0', board, strategy)
    game = GuiGame(p1, p2, board)
    root = tkinter.Tk()
    my_gui = Gui(root, game)
    root.mainloop()

if __name__ == '__main__':
    #TODO: specifications and tests
    main()
