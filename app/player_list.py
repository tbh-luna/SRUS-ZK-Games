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

        # Makes new node from player.
        newNode = PlayerNode(player)
        oldHead = self.__listHead

        # If head is empty
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

        # If tail empty
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

            # New node next is none for it is the tail.
            newNode.next_set(None)

    def pop_at_head(self):
        if not self.head_is_not_empty():
            return

        # At first i just set head to next node
        # But then i realised that working backwards still had a reference to it
        # So this instead

        # Also im using multiple single line comments because I don't like how the triple quotes look
        # I wish python had /* sometimes.
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

                # Iterates through each node and tries to pop it by matching its ID

                while True:
                    if workingNode is None:
                        print("No Node with ID found.")
                        return

                    if workingNode.key == xid:


                        nextNode = workingNode.next_get
                        previousNode = workingNode.previous_get

                        if previousNode is not None:
                            previousNode.next_set(nextNode)
                        if nextNode is not None:
                            nextNode.previous_set(previousNode)

                        if workingNode == self.__listTail:
                            self.__listTail = previousNode

                        del workingNode
                        return

                    else:
                        if workingNode.next_get is None:
                            break

                        workingNode = workingNode.next_get

    def display(self, fromhead):

        if fromhead:
            if self.head_is_not_empty():
                workingNode = self.__listHead

            else:
                workingNode = None

            while workingNode is not None:
                # So here I initially tried to just print out the str representation of the classes?
                # but it ended up causing a recursion error (maximum recursion depth exceeded)
                # I tried reformatting, looking up how to do __str__ functions,
                # but no matter what I've done it hasn't worked. I don't know what I'm doing wrong
                # I tried removing references to other classes, leaving only variables
                # I don't know and at this point this is overdue as is.
                print(f'Player ID : {workingNode.key}, Player Name : {workingNode.player_get.name}')
                workingNode = workingNode.next_get

        else:
            if self.tail_is_not_empty():
                workingNode = self.__listTail

            else:
                print("Tail is empty")
                return

            while workingNode is not None:

                print(f'Player ID : {workingNode.key}, Player Name : {workingNode.player_get.name}')
                workingNode = workingNode.previous_get

                if workingNode is None:
                    return

    def __str__(self):
        return f'Head: {self.__listHead} Tail: {self.__listTail}'







