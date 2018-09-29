# Binary Tree

A binary tree is one of the most typical tree structure. As the name suggests, a
binary tree is a tree data structure in which each node has ```at most two children```,
which are referred to as the left child and the right child

## Overview
* Understand the concept of a ```tree``` and a ```binary tree```
* Be familiar with different ```traversal``` methods
* Use ```recursion``` to solve binary-tree-related problems

## Traverse a Tree

### Pre-order Traversal
* Pre-order traversal is to visit the root first. Then traverse the left subtree.
Finally, traverse the right subtree.

### In-order Traversal
* In-order traversal is to traverse the left subtree first. Then visit the root.
Finally, traverse the right subtree.
* Typically, for ```binary search tree```, we can retrieve all the data in sorted order using
in-order traversal

### Post-order Traversal
* Post-order traversal is to traverse the left subtree first. Then traverse the right subtree.
Finally, visit the root.
