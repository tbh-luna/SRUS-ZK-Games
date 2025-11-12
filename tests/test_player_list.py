import unittest
from src.player import Player
from src.player_list import PlayerList


class MyTestCase(unittest.TestCase):
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

    def test_pop_head(self):

        self.player_list.insert_at_head(self.player)
        self.assertEqual(self.player_list.head.key, self.player.uid)
        self.player_list.pop_at_head()
        self.assertEqual(self.player_list.head, None)
        self.player_list.insert_at_head(self.player)

        self.player_list.insert_at_head(self.player2)
        self.assertEqual(self.player_list.head.key, self.player2.uid)
        self.player_list.pop_at_head()
        self.assertEqual(self.player_list.head.key, self.player.uid)

    def test_pop_tail(self):

        self.player_list.insert_at_tail(self.player)
        self.assertEqual(self.player_list.tail.key, self.player.uid)
        self.player_list.pop_at_tail()
        self.assertEqual(self.player_list.tail, None)
        self.player_list.insert_at_tail(self.player)

        self.player_list.insert_at_tail(self.player2)
        self.assertEqual(self.player_list.tail.key, self.player2.uid)
        self.player_list.pop_at_tail()
        self.assertEqual(self.player_list.tail.key, self.player.uid)

    def test_pop_by_id(self):

        self.player_list.insert_at_head(self.player)
        self.player_list.insert_at_head(self.player2)
        self.player_list.insert_at_head(self.player3)
        self.assertEqual(self.player_list.head.key, self.player3.uid)
        self.player_list.pop_using_id("1")
        self.assertEqual(self.player_list.head.key, self.player3.uid)
        self.assertEqual(self.player_list.tail.key, self.player2.uid)
        self.player_list.display(True)

if __name__ == '__main__':
    unittest.main()
