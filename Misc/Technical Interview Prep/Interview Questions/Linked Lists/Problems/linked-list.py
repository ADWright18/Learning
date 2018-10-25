"""
Problem Description:
    Write code to remove duplicates from an unsorted linked list.
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class LinkedList:

    def __init__(self, node):
        self.head = node

    def __str__(self):
        n = self.head
        s = "start"

        while (n != None):
            s = s + " -> " + str(n.data)
            n = n.next
        return s

    def append(self, value):
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


# Main Program
a = Node(20)
d = LinkedList(a)
d.append(6)
d.append(9)
d.append(9)
d.append(6)
print(d)
print(d.returnKthToLast(1))
