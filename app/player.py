class Player:
    def __init__(self, id, playerName):
        self.id = id
        self.playerName = playerName

    @property
    def __uid(self):
        return self.id

    @property
    def __name(self):
        return self.playerName

    def __str__(self):
        print("Player name:", self.__name(), "ID:", self.__uid())
