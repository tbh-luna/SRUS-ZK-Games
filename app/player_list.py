from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__listHead = None
        self.__listTail = None

    def head_is_not_empty(self):
        if self.__listHead is None:
            return False
        else:
            return True

    def tail_is_not_empty(self):
        if self.__listTail is None:
            return False
        else:
            return True

    def insert_at_head(self, player):

        # makes new node from player.
        newNode = PlayerNode(player)

        # if head isn't empty
        if self.head_is_not_empty():
            newNode.next_set = self.__listHead

        # new node previous is none, for it is the head.
        newNode.previous_set = None
        self.__listHead = newNode

    def insert_at_tail(self, player):
        newNode = PlayerNode(player)

        if self.tail_is_not_empty():
            newNode.previous_set = self.__listTail

        # new node next is none for it is the tail..
        newNode.next_set = None
        self.__listTail = newNode

    def pop_at_head(self):
        if not self.head_is_not_empty():
            return
        else:
            self.__listHead = self.__listHead.next_get

    def pop_at_tail(self):
        if not self.tail_is_not_empty():
            return
        else:
            self.__listTail = self.__listTail.previous_get









