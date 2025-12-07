from __future__ import annotations
from src.player import Player


class PlayerBNode:
    def __init__(self, player : Player):
        self.__internalPlayer = player
        self.__leftNode = None
        self.__rightNode = None

    @property
    def internalPlayer(self):
        return self.__internalPlayer

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

    def __eq__(self, other):
        return len(self.internalPlayer.name) == len(other.name)

    def __lt__(self, other):
        return len(self.internalPlayer.name) < len(other.name)

    def __gt__(self, other):
        return len(self.internalPlayer.name) > len(other.name)

    def __ge__(self, other):
        return len(self.internalPlayer.name) >= len(other.name)

    def __le__(self, other):
        return len(self.internalPlayer.name) <= len(other.name)

    def __ne__(self, other):
        return len(self.internalPlayer.name) != len(other.name)
