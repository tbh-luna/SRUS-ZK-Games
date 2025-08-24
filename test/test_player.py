import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(1, "Zoe")

    def test_ids(self):
        self.assertEqual(self.player.uid, 1)
        self.assertEqual(self.player.name, "Zoe")

if __name__ == '__main__':
    unittest.main()