import unittest
from app.player import Player
from app.player_list import PlayerList

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, "Zoe")
        self.player_list = PlayerList()

    def test_ids(self):
        self.assertEqual(self.player.uid, 1)
        self.assertEqual(self.player.name, "Zoe")

if __name__ == '__main__':
    unittest.main()