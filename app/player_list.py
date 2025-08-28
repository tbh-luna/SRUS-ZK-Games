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

            if not self.tail_is_not_empty():
                self.__listTail = self.__listHead
                self.__listTail.next_set = None
                self.__listTail.previous_set = newNode

        # new node previous is none, for it is the head.
        newNode.previous_set = None
        self.__listHead = newNode

    def insert_at_tail(self, player):
        newNode = PlayerNode(player)

        if self.tail_is_not_empty():
            newNode.previous_set = self.__listTail

            if not self.head_is_not_empty():
                self.__listHead = self.__listTail
                self.__listHead.previous_set = None
                self.__listHead.next_set = newNode

        # new node next is none for it is the tail.
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

    def pop_using_id(self, xid):

        if self.head_is_not_empty():
            if self.__listHead.key == xid:
                self.__listHead = self.__listHead.next_get
                self.__listHead.previous_set = None
                return

            else:
                workingNode = self.__listHead.next_get

                while True:
                    if workingNode is None:
                        print("No Node with ID found.")
                        return

                    if workingNode.key == xid:
                        nextNode = workingNode.next_get
                        previousNode = workingNode.previous_get
                        previousNode.next_set = nextNode
                        nextNode.previous_set = previousNode
                        del workingNode
                        return

                    else:
                        workingNode = workingNode.next_get

        if self.tail_is_not_empty():
            return






