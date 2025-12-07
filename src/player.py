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

        """
        Hashes the password using Argon2.
        saves object hash

        Args:
            password: The password to be hashed.
        """

        self.__hash = PasswordHasher().hash(password)

    def check_password(self, password : str):

        """
        Checks whether password matches hash.

        Args:
            password: The password to be checked.

        Raises:
            argon2.exceptions.VerifyMismatchError:
            if password does not match.
        """

        PasswordHasher().verify(self.__hash, password)

    def __str__(self):

        """
        String representation of Player.

        Returns:
            str: Readable representation of Player.
        """

        return f'Player ID: {self.__ID} Name: {self.__playerName}'

    def __eq__(self, other):

        """
        Equality check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is equal to the other player's.
        """

        return int(self.score) == int(other.score)

    def __lt__(self, other):

        """
        Less than check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is less than the other player's.
        """

        return int(self.score) < int(other.score)

    def __gt__(self, other):

        """
        Greater than check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is greater than the other player's.
        """

        return int(self.score) > int(other.score)

    def __ge__(self, other):

        """
        Greater equals check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is greater than, or equal to the other player's.
        """

        return int(self.score) >= int(other.score)

    def __le__(self, other):

        """
        Less equals check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is less than, or equal to the other player's.
        """

        return int(self.score) <= int(other.score)

    def __ne__(self, other):

        """
        Not equals check.

        Args:
            other: The other player.

        Returns:
            bool: True if player score is not equal to the other player's.
        """

        return int(self.score) != int(other.score)

    # I chose bubble sort because it is simple to implement,
    # And this does not have to be terribly performant.

    @staticmethod
    def bubble_sort(playerList : list[Player]):

        """
        Sorts a list of players by score.

        Args:
            playerList [list[Player]]: List containing player objects to be sorted.

        Returns:
             None
        """

        for i in playerList:
            for x in range(0, len(playerList) - 1):
                if playerList[x] < playerList[x + 1]:
                    temp = playerList[x]
                    playerList[x] = playerList[x + 1]
                    playerList[x + 1] = temp
