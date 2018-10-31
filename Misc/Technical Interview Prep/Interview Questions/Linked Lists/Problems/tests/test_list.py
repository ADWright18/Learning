import pytest

from linkedlist import Node, LinkedList

def test_node_attributes():
    head = Node(1)
    assert head.prev is None
    assert head.next is None

    previous = Node(0)
    head.prev = previous
    assert head.prev is previous
    assert head.next is None
    assert head.data == 1
    assert head.prev.prev is None
    assert head.prev.data == 0
    assert repr(previous) == "Node(0)"

    next = Node(2)
    head.next = next
    assert head.prev is previous
    assert head.next is next
    assert head.data == 1
    assert head.next.next == None
    assert head.prev.prev == None
    assert head.next.data == 2
    assert repr(next) == "Node(2)"

def test_list_attributes():
    # Test Empty List
    empty_list = LinkedList()
    assert str(empty_list) == ""
    empty_list.append(0)
    assert str(empty_list) == "0"
    assert type(empty_list.head) == Node

    # Test List (Initialized with a Node)
    a = Node(0)
    linked_list = LinkedList(a)
    assert linked_list.head == a
    assert linked_list.head.data == 0
    assert linked_list.head.prev == None
    assert str(linked_list) == "0"

    linked_list.append(1)
    assert linked_list.head.next.data == 1
    assert str(linked_list) == "0 -> 1"

    linked_list.append([2,3,4])
    assert str(linked_list) == "0 -> 1 -> 2 -> 3 -> 4"

    # Test iteration through a linked list
    n = linked_list.head
    temp = []

    while (n != None):
        temp.append(n.data)
        n = n.next

    assert temp == [0,1,2,3,4]

    # Test reverse iteration through a linked list
    n = linked_list.head
    reverse_temp = []

    while (n.next != None): # Get to the end
        n = n.next

    while (n != None):
        reverse_temp.append(n.data)
        n = n.prev

    assert reverse_temp == [4,3,2,1,0]


def test_list_methods():
    linked_list = LinkedList()
    linked_list.append([3,3,4,5,2,4])

    # Test removeDuplicates()
    linked_list.removeDuplicates()

    # Test iteration through a linked list
    n = linked_list.head
    temp = []

    while (n != None):
        temp.append(n.data)
        n = n.next

    assert temp == [3,4,5,2]

    # Test reverse iteration through a linked list
    n = linked_list.head
    reverse_temp = []

    while (n.next != None): # Get to the end
        n = n.next

    while (n != None):
        reverse_temp.append(n.data)
        n = n.prev

    assert reverse_temp == [2,5,4,3]

    # Test returnKthToLast()
    linked_list = LinkedList()
    linked_list.append([3,8,5,9,4])

    k = 2
    assert 9 == linked_list.returnKthToLast(k)
