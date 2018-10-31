# Stack
* The stack is a data structure that acts like a stack of data
* A stack uses LIFO (last-in first-out) ordering.

## Implementing a Stack
* A stack uses the following operations
  * pop(): Remove the top item from the stack
  * push(item): Add an item to the top of the stack
  * peek(): Return the top of the stack
  * isEmpty(): Return true if and only if the stack is empty

* Unlike an array, a stack does not offer constant-time access to the ith item
* However, it does allow constant-time adds and removes, as it doesn't require
shifting elements around
