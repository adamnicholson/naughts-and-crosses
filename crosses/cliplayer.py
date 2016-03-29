from crosses.board import Board
from crosses.player import Player


class CliPlayer(Player):

    def __init__(self, my_player_number: int):
        self.my_player_number = my_player_number

    def prompt(self, my_player_number: int, board: Board):
        pos = "0"
        options = board.available()
        while int(pos) not in options:
            pos = input("Choose your move (" + ",".join(map(str, options)) + ")")

        return pos