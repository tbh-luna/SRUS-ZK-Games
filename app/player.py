from argon2 import PasswordHasher

class Player:
    def __init__(self, __ID : int, __playerName : str):
        self.__ID = __ID
        self.__playerName = __playerName
        self.__hash = None
        self.__score = 0

    @property
    def uid(self) -> int:
        return self.__ID

    @property
    def name(self) -> str:
        return self.__playerName

    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, value : int):
        assert value > 0
        self.__score = value

    def add_password(self, password : str):
        self.__hash = PasswordHasher().hash(password)

    def check_password(self, password : str):
        PasswordHasher().verify(self.__hash, password)

    def __str__(self):
        return f'Player ID: {self.__ID} Name: {self.__playerName}'
