import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player(1, "Luna")
        self.player.__str__()

if __name__ == '__main__':
    unittest.main()