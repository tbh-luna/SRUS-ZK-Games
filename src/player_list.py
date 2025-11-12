from src.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        self.__listHead = None
        self.__listTail = None
        self.fromhead = True

    @property
    def head(self):
        return self.__listHead

    @property
    def tail(self):
        return self.__listTail

    def head_is_not_empty(self):

        """Checks if head is not empty.
        In hindsight should have checked
        whether head IS empty.

        Returns: Boolean
        """

        if self.__listHead is None:
            return False
        else:
            return True

    def tail_is_not_empty(self):

        """Checks if tail is not empty.

        Returns: Boolean
        """

        if self.__listTail is None:
            return False
        else:
            return True

    def insert_at_head(self, player):

        """Inserts a node at the head

        Args:
        Player: The node being inserted
        """

        # Makes new node from player.
        newNode = PlayerNode(player)
        oldHead = self.__listHead

        # If head is empty
        if not self.head_is_not_empty():
            self.__listHead = newNode
            self.__listHead.previous = None
            if not self.tail_is_not_empty():
                self.__listHead.next = None

        else:
            self.__listHead = newNode
            self.__listHead.next = oldHead
            oldHead.previous = newNode

            if not self.tail_is_not_empty():
                self.__listTail = oldHead
                self.__listTail.next = None
                self.__listTail.previous = newNode

        self.__listHead.previous = None
        return

    def insert_at_tail(self, player):

        """Inserts a node at tail

        Args:
        Player: The node being inserted
        """

        newNode = PlayerNode(player)
        oldTail = self.__listTail

        # If tail empty
        if not self.tail_is_not_empty():
            self.__listTail = newNode
            newNode.next = None
            return

        else:

            self.__listTail = newNode
            newNode.previous = oldTail
            oldTail.next = newNode

            if not self.head_is_not_empty():
                self.__listHead = oldTail
                self.__listHead.previous = None
                self.__listHead.next = newNode

            # New node next is none for it is the tail.
            newNode.next = None

    def pop_at_head(self):

        """Pops node at head
        replaces head as necessary.
        """

        if not self.head_is_not_empty():
            return

        else:
            if self.__listHead.next is None:

                if self.tail_is_not_empty():
                    if self.__listTail.previous == self.__listHead:
                        self.__listTail.previous = None
                    if self.__listTail == self.__listHead:
                        self.__listTail = None

                workingNode = self.__listHead
                self.__listHead = None
                del workingNode

                return

            workingNode = self.__listHead
            comingNode = workingNode.next
            comingNode.previous = None
            self.__listHead = comingNode
            del workingNode

    def pop_at_tail(self):

        """Pops node at tail
        replaces tail as necessary.
        """

        if not self.tail_is_not_empty():
            return

        else:
            if self.__listTail.previous is None:
                workingNode = self.__listTail
                self.__listTail = None
                del workingNode
                return

            workingNode = self.__listTail
            comingNode = workingNode.previous
            comingNode.next = None
            self.__listTail = comingNode
            del workingNode

    def pop_using_id(self, xid : str):

        """Pops a node from the list
        iterating from head
        using specified ID

        Args:
            xid: The node ID
        """

        if self.head_is_not_empty():
            if self.__listHead.key == xid:
                self.__listHead = self.__listHead.next
                self.__listHead.previous = None
                return

            else:
                workingNode = self.__listHead.next

                # Iterates through each node and tries to pop it by matching its ID

                while True:
                    if workingNode is None:
                        print("No Node with ID found.")
                        return

                    if workingNode.key == xid:

                        nextNode = workingNode.next
                        previousNode = workingNode.previous

                        if previousNode is not None:
                            previousNode.next = nextNode
                        if nextNode is not None:
                            nextNode.previous = previousNode

                        if workingNode == self.__listTail:
                            self.__listTail = previousNode

                        del workingNode
                        return

                    else:
                        if workingNode.next is None:
                            break

                        workingNode = workingNode.next
        else:
            print("List is empty.")

    def display(self, fromhead : bool):

        """Displays the list
        Starting from either the head,
        or the tail, going
        forwards or backwards
        respectively.

        Args:
            fromhead: if false, goes from tail.
            if true, goes from head.
        """

        if fromhead:
            if self.head_is_not_empty():
                workingNode = self.__listHead

            else:
                workingNode = None

            while workingNode is not None:

                print(workingNode)
                workingNode = workingNode.next

        else:
            if self.tail_is_not_empty():
                workingNode = self.__listTail

            else:
                print("Tail is empty")
                return

            while workingNode is not None:

                print(workingNode)
                workingNode = workingNode.previous

                if workingNode is None:
                    return

    def __str__(self):
        return f'Head: {self.__listHead} Tail: {self.__listTail}'
