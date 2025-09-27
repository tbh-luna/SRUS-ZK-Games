class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__nextNode = None
        self.__previousNode = None

    @property
    def player_get(self):
        return self.__player

    @property
    def next(self):
        return self.__nextNode


    @next.setter
    def next(self, value):
        self.__nextNode = value

    @property
    def previous(self):
        return self.__previousNode

    @previous.setter
    def previous(self, value):
        self.__previousNode = value

    @property
    def key(self):
        return self.__player.uid

    def __str__(self):
        return f'Player Node: ({self.__player})'
