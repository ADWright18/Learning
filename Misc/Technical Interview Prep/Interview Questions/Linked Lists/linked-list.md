# Linked Lists
* A linked list is a data structure that represents a sequence of nodes
* In a singly linked list, each node points to the next node in the linked list.
* A doubly linked list gives each node pointers to both the next node and the
previous node.
* Note: Unlike an array, a linked list does not provide constant time (O(1))
access to a particular "index" within the list
* Note: However, you can add and remove items from the beginning in constant
time

## Creating a Linked List
* The code below implements a very basic singly linked list.

```java
class Node {
  Node next = null;
  int data;

  public Node(int d) {
    data = d;
  }

  void appendToTail(int d) {
    Node end = new Node(d);
    Node n = this;
    while (n.next != null) {
      n = n.next;
    }
    n.next = end;
  }
}
```

* In this implementation, we don't have a LinkedList data structure (list only
  accessible through a reference to the head Node).

* We could implement a LinkedList class that wraps the Node class.
  * LinkedList class would have one member variable: the head Node

## Deleting a Node from a Singly Linked List
* Given a node n, we find the previous node, ```prev```, and set ```prev.next```
equal to ```n.next```.
* If the list is doubly linked, we must also update ```n.next``` to set ```n.next.prev```
equal to ```n.prev```.
* Note: If you implement this code in C, C++ or another language that requires
the developer to do memory management, you should consider if the removed node
should be deallocated

```java
Node deleteNode(Node head, int d) {
  Node n = head;

  if (n.data == d) {
    return head.next; /* moved head */
  }

  while (n.next != null) {
    if (n.next.data == d) {
      n.next = n.next.next;
      return head; /* head didn't change */
    }
    n = n.next;
  }
  return head
}
```

## The "Runner" Technique
* The "runner" (or second pointer) technique is used in many linked list
problems.
* The runner technique means that you iterate through the linked list with two
pointers simultaneously, with one ahead of the other.
* The "fast" node might be ahead by a fixed amount, or it might be hopping
multiple nodes for each one node that the "slow" node iterates through
