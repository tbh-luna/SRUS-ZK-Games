import unittest
from app.player import Player
from app.player_list import PlayerList
from app.player_node import PlayerNode

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, "Zoe")
        self.player2 = Player(2, "Luna")
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

if __name__ == '__main__':
    unittest.main()