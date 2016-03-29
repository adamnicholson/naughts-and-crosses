import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/..'))
import unittest
from crosses import Board


class TestBoard(unittest.TestCase):

    def test_all_positions_are_available_on_new_board(self):
        board = Board()
        self.assertEqual([1,2,3,4,5,6,7,8,9], board.available())

    def test_used_positions_are_removed_from_available_list(self):
        board = Board()
        board.move(1, 1)
        self.assertEqual([2,3,4,5,6,7,8,9], board.available())
        board.move(2, 2)
        self.assertEqual([3,4,5,6,7,8,9], board.available())
        board.move(1, 6)
        self.assertEqual([3,4,5,7,8,9], board.available())
        board.move(2, 7)
        self.assertEqual([3,4,5,8,9], board.available())


if __name__ == '__main__':
    unittest.main()