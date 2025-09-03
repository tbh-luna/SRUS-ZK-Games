class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__nextNode = None
        self.__previousNode = None

    @property
    def player_get(self):
        return self.__player

    @property
    def next_get(self):
        return self.__nextNode

    def next_set(self, value):
        self.__nextNode = value

    @property
    def previous_get(self):
        return self.__previousNode

    def previous_set(self, value):
        self.__previousNode = value

    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f'PlayerNode: {self.__player} Next Node: {self.__nextNode}  Previous Node: {self.__previousNode}'
