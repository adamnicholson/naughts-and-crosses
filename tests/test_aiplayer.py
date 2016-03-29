import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..'))
import unittest
from crosses import AIPlayer, Board


class TestAiPlayer(unittest.TestCase):

    def test_chooses_obvious_winning_move_if_winnable_in_one(self):
        ai = AIPlayer(1)

        states = (
            ({1:1, 2:1, 4:2, 7:2}, 3),
            ({1:1, 2:1, 3:2, 4:1, 6:2, 8:2}, 7)
        )

        for test in states:
            board = Board()
            board.used = test[0]
            self.assertEqual(test[1], ai.prompt(board))


if __name__ == '__main__':
    unittest.main()