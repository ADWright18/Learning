import pytest

from linkedlist import Node, LinkedList

import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def test_node_attributes():
    head = Node(1)
    assert head.prev is None
    assert head.next is None
