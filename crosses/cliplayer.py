from crosses.board import Board
from crosses.player import Player


class CliPlayer(Player):

    def __init__(self, my_player_number: int):
        self.my_player_number = my_player_number

    def prompt(self, board: Board):
        pos = 0
        options = board.available()
        while pos not in options:
            pos = input("Choose your move. Remaining options are " + ",".join(map(str, options)) + ": ")
            try:
                pos = int(pos)
            except ValueError:
                pos = 0

        return pos