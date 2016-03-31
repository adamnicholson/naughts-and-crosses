import copy
import random

from crosses.board import Board
from crosses.player import Player


class AIPlayer(Player):

    def __init__(self, my_player_number: int):
        self.my_player_number = my_player_number

    def prompt(self, board: Board):

        print("Board: " + str(board.used))
        bestMove = None
        bestMoveScore = None

        for pos in board.available():

            score = self.scoreMove(board, self.my_player_number, pos)

            print("AI rekons move " + str(pos) + " is worth " + str(score))

            if bestMove is None or score > bestMoveScore:
                bestMoveScore = score
                bestMove = pos

        return bestMove

    def opponent(self, player: int):
        return 1 if player == 2 else 1

    # Determine the value of this move, given a board in the given state.
    def scoreMove(self, board: Board, player: int, move: int) -> int:

        if player == 1:
            opponent = 2
        else:
            opponent = 1

        board = copy.deepcopy(board)
        board.move(player, move)

        if board.over():
            if board.iswinner(player):
                # This move causes me to win. Value should be "1"
                return 1
            else:
                # This move is the final space on the board, and causes a draw. Value should be "0"
                return 0

        branch_scores = []
        for pos in board.available():
            # Determine the opponent's score for this branch
            opponents_branch_score = self.scoreMove(board, opponent, pos)

            # We have the opposite goal of the opponent. If they achieve a 10 for this branch, then we
            # consider this to be -10, and vice-versa. So let's say *our* score for this branch
            # is the inverse of the opponents score
            branch_score = -opponents_branch_score
            branch_scores.append(branch_score)

        return sum(branch_scores) / len(branch_scores)
