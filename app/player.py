class Player:
    def __init__(self, ID, playerName):
        self.ID = ID
        self.playerName = playerName

    @property
    def __uid(self):
        return self.ID

    @property
    def __name(self):
        return self.playerName

    def __str__(self):
        print("Player name: " + self.playerName + " ID:" + self.ID())
