from __future__ import annotations
from src.player import Player
from src.player_bnode import PlayerBNode


class PlayerBST:
    def __init__(self):
        self.__treeRoot = None

    @property
    def treeRoot(self):
        return self.__treeRoot

    def insert(self, player : Player, workingNode : PlayerBNode) -> None:

        """
        Inserts a player into the tree.
        Args:
            player: The player to insert into the tree.
            workingNode: The node currently being worked on
                        (Should be root at first.)
        Returns:
            Nothing
        """

        if self.__treeRoot is None:
            self.__treeRoot = PlayerBNode(player)
            return

        if workingNode < player:
            if workingNode.leftNode is None:
                workingNode.leftNode = PlayerBNode(player)
                return

            else:
                workingNode = workingNode.leftNode
                self.insert(player, workingNode)
                return

        elif workingNode > player:
            if workingNode.rightNode is None:
                workingNode.rightNode = PlayerBNode(player)
                return

            else:
                workingNode = workingNode.rightNode
                self.insert(player, workingNode)
                return

        elif workingNode == player:
            print("No duplicate keys")
            return
