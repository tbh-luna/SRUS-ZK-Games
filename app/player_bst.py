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

        if workingNode is None:
            workingNode = PlayerBNode(player)



