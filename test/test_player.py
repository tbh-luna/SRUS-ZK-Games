import unittest
from app.player import Player
from app.player_list import PlayerList

class TestPlayer(unittest.TestCase):

    # These should cover most functionalities of the lists and they run fine.
    # I'm sure there are edge cases or things I've forgotten about. Please feel free to email me about the,.

    def setUp(self):
        self.player = Player(1, "Zoe")
        self.player2 = Player(2, "Luna")
        self.player3 = Player(3, "Mars")
        self.player_list = PlayerList()

    def test_ids(self):
        self.assertEqual(self.player.uid, 1)
        self.assertEqual(self.player.name, "Zoe")

    def test_pop_head(self):

        self.player_list.insert_at_head(self.player)
        self.assertEqual(self.player_list.get_head.key, self.player.uid)
        self.player_list.pop_at_head()
        self.assertEqual(self.player_list.get_head, None)
        self.player_list.insert_at_head(self.player)

        self.player_list.insert_at_head(self.player2)
        self.assertEqual(self.player_list.get_head.key, self.player2.uid)
        self.player_list.pop_at_head()
        self.assertEqual(self.player_list.get_head.key, self.player.uid)

    def test_pop_tail(self):

        self.player_list.insert_at_tail(self.player)
        self.assertEqual(self.player_list.get_tail.key, self.player.uid)
        self.player_list.pop_at_tail()
        self.assertEqual(self.player_list.get_tail, None)
        self.player_list.insert_at_tail(self.player)

        self.player_list.insert_at_tail(self.player2)
        self.assertEqual(self.player_list.get_tail.key, self.player2.uid)
        self.player_list.pop_at_tail()
        self.assertEqual(self.player_list.get_tail.key, self.player.uid)

    def test_pop_by_id(self):
        self.player_list.insert_at_head(self.player)
        self.player_list.insert_at_head(self.player2)
        self.player_list.insert_at_head(self.player3)
        self.assertEqual(self.player_list.get_head.key, self.player3.uid)
        self.player_list.pop_using_id(1)
        self.assertEqual(self.player_list.get_head.key, self.player3.uid)
        self.assertEqual(self.player_list.get_tail.key, self.player2.uid)
        self.player_list.display(True)



if __name__ == '__main__':
    unittest.main()