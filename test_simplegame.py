import unittest
import SOS


class TestSos(unittest.TestCase):

    # Checking the board dimension
    def test_board(self):
        Board = SOS.board
        size = SOS.board_size
        self.assertEqual(len(Board), size)

    # This test is used to check whether S for Blue player and O for red player is displayed on the first row after
    # 3 turns (Blue player plays first)
    def test_display(self):
        Board = SOS.board
        self.assertEqual(Board[0], ['S', 'O', 'S'])

    # This test is used to check the current turn is Red after 3 turns (Blue player plays first)
    def test_turn(self):
        signs = SOS.sign
        turns = SOS.turn
        self.assertEqual(signs, 3)
        self.assertEqual(turns, 'Blue')

    # This test is used to check whether the mode is Simple Game when the player hits the simple game button
    def test_Gamemode(self):
        mode = SOS.GameMode.get()
        self.assertEqual(mode, 'Simple Game')

    # This test is used to check the function isFull returns True when the board is filled up
    def test_isFull(self):
        full = SOS.isfull()
        self.assertEqual(full, True)

