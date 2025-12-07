import unittest
from src.player import Player
from src.player_bst import PlayerBST


class TestPlayerBst(unittest.TestCase):

    def setUp(self):
        self.player = Player("1", "Zoe")
        self.player2 = Player("2", "Luna")
        self.player3 = Player("3", "He")
        self.player4 = Player("4", "Wayne")
        self.player5 = Player("5", "Prunsel")
        self.player_tree = PlayerBST()

    def test_insert(self):
        self.player_tree.insert(self.player, self.player_tree.treeRoot)
        self.player_tree.insert(self.player2, self.player_tree.treeRoot)
        self.player_tree.insert(self.player3, self.player_tree.treeRoot)
        self.player_tree.insert(self.player5, self.player_tree.treeRoot)

        self.assertEqual(self.player_tree.treeRoot.internalPlayer.name, self.player.name)
        self.assertEqual(self.player_tree.treeRoot.leftNode.internalPlayer.name, self.player2.name)
        self.assertEqual(self.player_tree.treeRoot.leftNode.leftNode.internalPlayer.name, self.player5.name)
        self.assertEqual(self.player_tree.treeRoot.rightNode.internalPlayer.name, self.player3.name)


if __name__ == '__main__':
    unittest.main()
