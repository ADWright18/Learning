# Hash Tables
* A hash table is a data structure that maps keys to values for highly efficient
lookup

* For a simple implementation, we use an array of linked lists and a hash code
function. To insert a key and value, we do the following:
  * First, compute the key's hash code
  * Then, map the hash code to an index in the array.
  * At this index, there is a linked list of keys and values. Store the key and
  value in this index.


* Note: We use a linked list to handle collisions

## Retrieve Value Pair by Key
* To retrieve the value pair by its key, you repeat this process.
  * Compute the hash code
  * Compute the index from the hash code
  * Search through the linked list for the value with this key


* If the number of collisions is very high, the worst case runtime is O(N), where N is the number of keys

* However, we generally assume a good implementation that keeps collisions to a minimum, in which case the lookup time is O(1)

* Alternatively, we can implement the hash table with a balanced binary search tree.
  * This gives us an O(log N) lookup time.
  * The advantage of the is potentially using less space, since we no longer allocate a large array
