# Tree
* A tree is a data structure composed of nodes
  * Each tree has a root node.
  * The root node has zero or more child nodes
  * Each child node has zero or more child nodes, and so on

* The tree cannot contain cycles and the nodes may or may not be in a particular
order
* A node is called a "leaf" node if it has no children

## Implementation of a Tree
* A very simple implementation of a tree node:

```java
class Node {
  public String name;
  public Node[] children;
}
```

* You might also have a Tree class to wrap this node.

```java
class Tree {
  public Node root;
}
```

* Tree and graph questions are rife with ambiguous details and incorrect
assumptions. Be sure to watch out for the following issues and seek clarification
when necessary

## Trees vs. Binary Trees
* A binary tree is a tree in which each node has up to two children.
* Not all trees are binary trees.

## Binary Tree vs. Binary Search Tree
* A binary search tree is a binary tree in which every node fits a specific
ordering property:
  * All left descendants <= n < all right descendants
* This must be true for each node n

## Balanced vs. Unbalanced
* While many trees are balanced, not all are.

## Complete vs. Not Complete
* A complete binary tree is a binary tree in which every level of the tree is
fully filled, except for perhaps the last level. To the extent that the last
level is filled, it is filled left to right.
