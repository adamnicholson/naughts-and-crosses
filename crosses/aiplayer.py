import copy
import random

from crosses.board import Board
from crosses.player import Player


class AIPlayer(Player):

    def prompt(self, my_player_number: int, board: Board):

        for pos in board.available():
            branch = copy.deepcopy(board)
            branch.move(my_player_number, pos)
            if branch.won():
                return pos



        return random.choice(board.available())