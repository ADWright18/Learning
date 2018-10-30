"""
Problem Description:
    Write code to remove duplicates from an unsorted linked list.
"""
class Node:
    """
    Represents a linked list node

    This class provides method and properties for managing
    the current node instance.

    Attributes
    ----------
    data : int
        value contained inside a node
    next : Node
        reference to the next node in the list
    prev : Node
        reference to the previous node in the list
    """
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self, node):
        self.head = node

    def __str__(self):
        n = self.head
        s = ""

        while (n != None):
            # Check if n is the head
            if (n.prev == None):
                s = s + str(n.data)
                n = n.next
                continue

            s = s + " -> " + str(n.data)
            n = n.next
        return s

    def append(self, value):
        """
        Append a value to the linked list

        This function creates a new node with the new value and
        sets it as the "next node" of the tail of the list

        Parameters
        ----------
        value : int
            value to append to the list

        Examples:
        """
        n = self.head

        # Travel to the end of the linked list
        previous = None
        while (n.next != None):
            previous = n
            n = n.next

        n.next = Node(value)

        # Add the prev value
        previous, n = n, n.next
        n.prev = previous


    def removeDuplicates(self):
        """
        Remove duplicates from the list

        This function removes all duplicated from the
        linked list by storing each unique value in a
        buffer and checking the buffer on each node.

        Examples:
        """
        # Store seen values
        buffer = []
        n = self.head

        # Keep track of previous value on current node
        previous = None

        # Iterate through the linked list
        while (n is not None):
            if (n.data in buffer):
                previous.next = n.next
            else:
                buffer.append(n.data)
                previous = n

            n = n.next

    def returnKthToLast(self, k):
        # Two pointers
        # counter - get the length of the list
        # n - get the kth last element
        counter = self.head
        n = self.head
        count = 0

        # Iterate through the list to get length
        while (counter is not None):
            count += 1
            counter = counter.next

        # Find the Kth element
        while (count != k):
            count -= 1
            n = n.next

        return n.data

    def deleteMiddleNode(self):
        # Two pointers
        # counter - get the length of list
        # n - delete the middle element
        counter = self.head
        n = self.head
        count = 0
        mid = 0

        # Iterate through the list to get length
        while (counter is not None):
            count += 1
            counter = counter.next

        # Check if the list contains at least > 2 elements
        if (count > 2):
            # Get the middle node (ceiling of count / 2)
            mid = -(-count // 2)
            while (count != mid + 1):
                count -= 1
                n = n.next
            n.next = n.next.next
        else:
            print("List needs to contain at least 3 elements: ")

    def partition(self, k):
        # Not finished*
        # Two pointers
        # swap - starts at the end of the list
        # n - starts at the beginning of the list
        swap = self.head
        n = self.head

        # Move swap to the end
        while (swap.next != None):
            swap = swap.next

        # Iterate through the list
        while (n != None):
            if (n.data < k):
                n = n.next
            elif (n.data >= k):
                n.data, swap.data = swap.data, n.data
                n = n.next
                swap = swap.prev

# Main Program
a = Node(20)
d = LinkedList(a)
d.append(9)
d.append(6)
d.append(7)
d.append(9)
print(d)
d.partition(20)
print(d)
