from player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.__listHead = None
        self.__listTail = None

    @property
    def get_head(self):
        return self.__listHead

    @property
    def get_tail(self):
        return self.__listTail

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
        oldHead = self.__listHead

        # if head is empty
        if not self.head_is_not_empty():
            self.__listHead = newNode
            self.__listHead.previous_set(None)

        else:
            self.__listHead = newNode
            self.__listHead.next_set(oldHead)
            oldHead.previous_set(newNode)

            if not self.tail_is_not_empty():
                self.__listTail = oldHead
                self.__listTail.next_set(None)
                self.__listTail.previous_set(newNode)

        self.__listHead.previous_set(None)
        return

    def insert_at_tail(self, player):

        newNode = PlayerNode(player)
        oldTail = self.__listTail

        # if tail empty
        if not self.tail_is_not_empty():
            self.__listTail = newNode
            newNode.next_set(None)
            return

        else:

            self.__listTail = newNode
            newNode.previous_set(oldTail)
            oldTail.next_set(newNode)

            if not self.head_is_not_empty():
                self.__listHead = oldTail
                self.__listHead.previous_set(None)
                self.__listHead.next_set(newNode)

            # new node next is none for it is the tail.
            newNode.next_set(None)

    def pop_at_head(self):
        if not self.head_is_not_empty():
            return

        # at first i just set head to next node
        # but then i realised that working backwards still had a reference to it lol
        # so this instead

        # also im using multiple single line comments because i dont like how the triple quotes look
        # i wish python had /* sometimes.
        else:
            if self.__listHead.next_get is None:
                workingNode = self.__listHead
                self.__listHead = None
                del workingNode
                return

            workingNode = self.__listHead
            comingNode = workingNode.next_get
            comingNode.previous_set(None)
            self.__listHead = comingNode
            del workingNode

    def pop_at_tail(self):

        if not self.tail_is_not_empty():
            return

        else:
            if self.__listTail.previous_get is None:
                workingNode = self.__listTail
                self.__listTail = None
                del workingNode
                return

            workingNode = self.__listTail
            comingNode = workingNode.previous_get
            comingNode.next_set(None)
            self.__listTail = comingNode
            del workingNode

    def pop_using_id(self, xid):

        if self.head_is_not_empty():
            if self.__listHead.key == xid:
                self.__listHead = self.__listHead.next_get
                self.__listHead.previous_set(None)
                return

            else:
                workingNode = self.__listHead.next_get

                # i enjoy while true loops
                # i used to not use them but using them has made my life like 10x easier. as is with programming.
                # you can end up with an infinite loop ofc. and that would be bad.
                # but i like to think i cover my bases
                # i wonder if eventually there will be a "while true considered harmful"
                while True:
                    if workingNode is None:
                        print("No Node with ID found.")
                        return

                    if workingNode.key == xid:
                        nextNode = workingNode.next_get
                        previousNode = workingNode.previous_get
                        previousNode.next_set(nextNode)
                        nextNode.previous_set(previousNode)
                        del workingNode
                        return

                    else:
                        workingNode = workingNode.next_get

        if self.tail_is_not_empty():
            return

    def display(self, fromhead):

        if fromhead:
            if self.head_is_not_empty():
                workingNode = self.__listHead
            else:
                workingNode = None
            while True:
                print(workingNode.key)
                workingNode = workingNode.next_get
                if workingNode is None:
                    break

        else:
            if self.tail_is_not_empty():
                workingNode = self.__listTail
            else:
                print("Tail is empty")
                return

            while True:

                print(workingNode.key)
                workingNode = workingNode.previous_get

                if workingNode is None:
                    return








