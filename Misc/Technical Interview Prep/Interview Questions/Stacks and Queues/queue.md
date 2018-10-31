# Queue
* A queue implements FIFO (first-in, first-out) ordering.
* As in a line or queue at a ticket stand, items are removed from the data
structure in the same order that they are added

## Implementing a Queue
* A queue uses the following operations:
  * add(item): Add an item to the end of the list
  * remove(): Remove the first item in the list
  * peek(): Return the top of the queue
  * isEmpty(): Return true if and only if the queue is empty

* Implementation of a queue using a linked list:

```java
public class MyQueue<T> {
  private static class QueueNode<T> {
    private T data;
    private QueueNode<T> next;

    public QueueNode(T data) {
      this.data = data;
    }
  }

  private QueueNode<T> first;
  private QueueNode<T> last;

  public void add(T item) {
      // Enqueue
      QueueNode<T> t = new QueueNode<T>(item);

      if (last != null) {
        last.next = t;
      }
      last = t;

      if (first == null) {
        first = last;
      }
  }

  public T remove() {
    // Dequeue
    if (first == null) throw new NoSuchElementException();

    T data = first.data;
    first = first.next;

    if (first == null) {
      last = null;
    }

    return data;
  }

  public T peek() {
    if (first == null) throw new NoSuchElementException();
    return first.data;
  }

  public boolean isEmpty() {
    return first == null;
  }
}
```

* One place where queues are often used is in breadth-first search or in
implementing a cache
* In BFS, for example, we used a queue to store a list of nodes that we need to
process. Each time we process a node, we add its adjacent nodes to the back of
the queue. This allows us to process nodes in the order in which they are viewed
