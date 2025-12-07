import unittest
import argon2
from src.player import Player
from src.player_list import PlayerList


class TestPlayer(unittest.TestCase):

    # These should hopefully cover most functionalities of the lists.

    def setUp(self):
        self.player = Player("1", "Zoe")
        self.player2 = Player("2", "Luna")
        self.player3 = Player("3", "Mars")
        self.player4 = Player("4", "Wayne")
        self.player5 = Player("5", "Prunsel")
        self.player_list = PlayerList()
        self.player.score = 1
        self.player2.score = 2
        self.player3.score = 3
        self.player4.score = 4
        self.player5.score = 4

        self.orderedList = [self.player4, self.player3, self.player2, self.player]
        self.disOrderedList = [self.player2, self.player4, self.player, self.player3]

        self.orderedDoubleUpList = [self.player5, self.player4,
                                    self.player3, self.player2]
        self.doubleUpList = [self.player2, self.player3, self.player5, self.player4]

    def test_ids(self):
        self.assertEqual(self.player.uid, "1")
        self.assertEqual(self.player.name, "Zoe")

    def test_password_check_correct(self):
        self.player.add_password("MicCheck1")
        self.player.check_password("MicCheck1")

    # Assert raises validates the test if there is a specific exception thrown.
    # (argon2.exceptions.VerifyMismatchError in this case)
    def test_password_check_incorrect(self):
        self.player.add_password("MicCheck1")
        with self.assertRaises(argon2.exceptions.VerifyMismatchError):
            self.player.check_password("MicCheck2")

    def test_ordered_list_sort(self):
        Player.bubble_sort(self.disOrderedList)
        self.assertEqual(self.orderedList, self.disOrderedList)

    def test_double_up_sort(self):
        Player.bubble_sort(self.doubleUpList)
        self.assertEqual(self.orderedDoubleUpList, self.doubleUpList)

    def test_comparisons(self):
        self.assertGreater(self.player2, self.player)
        self.assertLess(self.player, self.player3)
        self.assertNotEquals(self.player2, self.player4)
        self.assertEqual(self.player3, self.player3)

if __name__ == '__main__':
    unittest.main()
