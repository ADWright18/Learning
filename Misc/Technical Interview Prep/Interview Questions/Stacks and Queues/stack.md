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
* Implementation of a stack using a linked list:

```java
public class MyStack<T> {
  private static class StackNode<T> {
    private T data;
    private StackNode<T> next;

    public StackNode(T data) {
      this.data = data
    }
  }

  private StackNode<T> top;

  public T pop() {
    if (top == null) throw new EmptyStackException();
    T item = top.data;
    top = top.next;
    return item;
  }

  public void push(T item) {
    StackNode<T> t = new StackNode<T>(item);
    t.next = top;
    top = t;
  }

  public T peek() {
    if (top == null) throw new EmptyStackException();
    return top.data
  }

  public boolean isEmpty() {
    return top == null;
  }
}
```
