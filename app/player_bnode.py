from player import Player
from __future__ import annotations

class PlayerBNode:
    def __init__(self, player : Player):
        self.__internalPlayer = player
        self.__leftNode = None
        self.__rightNode = None

    @property
    def leftNode(self):
        return self.__leftNode

    @property
    def rightNode(self):
        return self.__rightNode

    @leftNode.setter
    def leftNode(self, node : PlayerBNode):
        self.__leftNode = node

    @rightNode.setter
    def rightNode(self, node : PlayerBNode):
        self.__rightNode = node
