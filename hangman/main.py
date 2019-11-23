from hangman.repository.sentences import Sentences
from hangman.service.service import Service
from hangman.ui.game import Game

if __name__ == '__main__':
    sentences = Sentences('sentences.txt')
    service = Service(sentences)
    game = Game(service)
    game.menu()