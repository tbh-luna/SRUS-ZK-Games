class Player:
    def __init__(self, __ID, __playerName):
        self.__ID = __ID
        self.__playerName = __playerName

    @property
    def uid(self):
        return self.__ID

    @property
    def name(self):
        return self.__playerName

    def __str__(self):
        print("Player name: " + str(self.name) + " ID:" + str(self.uid))
