# Hash Table

Hash Table is a data structure which organizes data using hash functions in order
to support quick insertion and search

## Types of Hash Tables
* Hash Set - a set data structure to store no repeated values
* Hash Map - a map data structure to store (key, value) pairs

## Collision Resolution
* If a hash function is a one-one mapping, we will not need to handle collisions.
* A collision resolution algorithm should solve the following questions:
  * How to organize the values in the same bucket?
  * What if too many values are assigned to the same bucket?
  * How to search a target value in a specific bucket?
* These questions are related to:
  * The capacity of the bucket
  * The number of keys
  * (which might be mapped into) the same bucket
* Let N be the max number of keys
  * If N is constant and small -> use an array to store keys in the same bucket
  * If N is variable and large -> use height-balanced search tree

## Complexity Analysis
* If there are M keys in total, we can achieve the space complexity of O(M)
* Ideally, the bucket size is small enough to be regarded as constant.
  * Insertion - O(1)
  * Search - O(1), if max bucket size is N -> O(N)

## Built-in Hash Table
* The typical design of a built-in hash table is:
  * The key value can be any hashable type. The value which belongs to a hashable
  type will have a hashcode - used in the mapping function to get the bucket index
  * Each bucket contains an array to store all the values in the same bucket initially
  * If there are too many values in the same bucket, these values will be maintained
  in a height-balanced binary search tree instead
* Time Complexity:
  * Average Case (search and insertion) - O(1)
  * Worse Case (search and insertion) - O(log N)

## Design the Key
* Let's look at an example:
```
Given an array of strings, group anagrams together
```
* A hash map can perform really well in grouping information by key. But we
cannot use the original string as key directly. We have to design a proper key to
present the type of anagrams.
* For instance, there are two strings "eat" and "ate" which should be in the same
group. While "eat" and "act" should not be grouped together

## Q & A
* What is the principle of hash table?
  * The key idea of a hash table is to use a hash function to map keys to buckets
  * Insertion - the hash function decides which bucket the key will be assigned
  * Search - the same hash function will find the key in the corresponding bucket
  * Example: y = x % 5

* What is the complexity of insertion and lookup operations?
