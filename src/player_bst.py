from __future__ import annotations
from player import Player
from player_bnode import PlayerBNode

class PlayerBST:

    def __init__(self):
        self.__treeRoot = None

    @property
    def treeRoot(self):
        return self.__treeRoot

    def insert(self, player : Player, workingNode : PlayerBNode) -> None:

        if self.__treeRoot is None:
            self.__treeRoot = PlayerBNode(player)
            return

        if workingNode.internalPlayer < player:
            workingNode = workingNode.leftNode
            self.insert(player, workingNode)
            return

        elif workingNode.internalPlayer > player:
            workingNode = workingNode.rightNode
            self.insert(player, workingNode)
            return

        elif workingNode.internalPlayer == player:
            print("No duplicate keys")
            return

