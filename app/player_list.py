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

    def insert_at_head(self, data):

        newNode = PlayerNode(data)

        if self.head_is_not_empty():
            newNode.next_set = self.__listHead
            if not self.tail_is_not_empty():
                self.__listTail = self.__listHead
                self.__listHead.next_set = None

        self.__listHead = newNode

        newNode.previous_set = None
        self.__listHead = newNode