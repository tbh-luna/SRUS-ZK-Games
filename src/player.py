from __future__ import annotations  # Here so I can typehint toward a 'player' object
from argon2 import PasswordHasher


class Player:
    def __init__(self, __ID : str, __playerName : str):
        self.__ID = __ID
        self.__playerName = __playerName
        self.__hash = None
        self.__score = 0

    @property
    def uid(self) -> str:
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

        """Hashes the password using Argon2.
        saves object hash

        Args:
            password: The password to be hashed.
        """

        self.__hash = PasswordHasher().hash(password)

    def check_password(self, password : str):

        """Checks whether password matches hash.

        Args:
            password: The password to be checked.

        Raises:
            argon2.exceptions.VerifyMismatchError:
            if password does not match.
        """

        PasswordHasher().verify(self.__hash, password)

    def __str__(self):
        return f'Player ID: {self.__ID} Name: {self.__playerName}'

    def __eq__(self, other):
        return int(self.score) == int(other.score)

    def __lt__(self, other):
        return int(self.score) < int(other.score)

    def __gt__(self, other):
        return int(self.score) > int(other.score)

    def __ge__(self, other):
        return int(self.score) >= int(other.score)

    def __le__(self, other):
        return int(self.score) <= int(other.score)

    def __ne__(self, other):
        return int(self.score) != int(other.score)

    # I chose bubble sort because it is easy to implement

    @staticmethod
    def bubble_sort(playerList : list[Player]):
        for i in playerList:
            for x in range(0, len(playerList) - 1):
                if playerList[x] < playerList[x + 1]:
                    temp = playerList[x]
                    playerList[x] = playerList[x + 1]
                    playerList[x + 1] = temp
