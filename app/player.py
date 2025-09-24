from argon2 import PasswordHasher

class Player:
    def __init__(self, __ID, __playerName):
        self.__ID = __ID
        self.__playerName = __playerName
        self.__hash = None

    @property
    def uid(self):
        return self.__ID

    @property
    def name(self):
        return self.__playerName

    def add_password(self, password):
        self.__hash = PasswordHasher().hash(password)

    def check_password(self, password):
        PasswordHasher().verify(self.__hash, password)

    def __str__(self):
        return f'Player ID: {self.__ID} Name: {self.__playerName}'
