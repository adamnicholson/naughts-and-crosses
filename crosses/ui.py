import sys

from crosses.board import Board
from crosses.player import Player


class UI:

    players = {}

    def __init__(self, board: Board, player1: Player, player2: Player):
        self.playerShapes = {
            1: 'X',
            2: 'O'
        }
        self.board = board
        self.players[1] = player1
        self.players[2] = player2

    def run(self):
        print("Welcome to naughts and crosses. Player 1 is crosses")
        player = 2

        while self.board.available():

            # Toggle to the next player
            if player == 1:
                print("Player 2 turn")
                player = 2
            elif player == 2:
                print("Player 1 turn")
                player = 1

            pos = self.players[player].prompt(self.board)
            self.board.move(player, pos)
            self.draw()

            # Check for victory condition
            if self.board.won():
                winner = self.board.winner()
                print("The game has been won by " + self.symbol(winner))
                exit()

        print("The game was a draw")

    def symbol(self, player):
        return self.playerShapes.get(player)

    def draw(self):

        for pos in self.board.positions:
            if pos in self.board.used.keys():
                player = self.board.used[pos]
                symbol = self.symbol(player)
            else:
                symbol = " "

            sys.stdout.write(symbol + ("\n" if (pos+1) % 3 == 1 else "|"))

        sys.stdout.write("\n")


