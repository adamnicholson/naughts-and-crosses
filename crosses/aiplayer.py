import copy
import random

from crosses.board import Board
from crosses.player import Player


class AIPlayer(Player):

    def __init__(self, my_player_number: int):
        self.my_player_number = my_player_number

    def prompt(self, board: Board):

        for pos in board.available():
            branch = copy.deepcopy(board)
            branch.move(self.my_player_number, pos)
            if branch.won():
                return pos

        return random.choice(board.available())

    def score(self, board: Board):
        if board.won() and board.winner() == self.my_player_number:
            return 10
        elif board.won() and board.winner() != self.my_player_number:
            return -10
        else:
            return 0
