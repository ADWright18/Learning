# Binary Search

Binary Search is one of the most fundamental and useful algorithms in CS. It
describes the process of searching for a specific value in an ordered collection

## Terminology
* Target - the value that you are searching for
* Index - the current location that you are searching
* Left, Right - the indices from which we use to maintain our search Space
* Mid - the index that we use to apply a condition to determine if we should
search left or right

## Identifying Binary Search
* Binary Search is an algorithm that divides the search space in 2 after every
comparison. Binary Search should be considered every time you need to search for
an index or element in a collection. If the collection is unordered, you can sort
it first before applying Binary Search.

## 3 Parts of a Successful Binary Search
* Pre-processing - sort if collection is unsorted
* Binary Search - Using a loop or recursion to divide search space in half after
each comparison
* Post-processing - Determine viable candidates in the remaining space

## 3 Templates for Binary Search
* Template 1:

```python
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # Define right, left
    r = len(nums) - 1
    l = 0

    while (l <= r):
        m = (l + r) // 2

        # Check if the target is present at the mid index
        if (nums[m] == target):
            return m
        # If target is greater, ignore left half
        elif (nums[m] < target):
            l = m + 1
        # If target is smaller, ignore right half
        elif (nums[m] > target):
              r = m - 1

    return -1
```

* Key Attributes
  * Search condition can be determined without comparing to the element's neighbors
  (or use specific elements around it)
  * No post-processing required because at each step, you are checking to see if
  the element has been found. If you reach the end, then you know the element
  is not found

* Distinguish Syntax
  * Initial Condition: ```left = 0, right = length - 1```
  * Termination: ```left > right```
  * Searching Left: ```right = mid - 1```
  * Searching Right: ```left = mid + 1```

* Template 2:

```python
def binarySearch(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  if (len(nums) == 0):
    return -1

  left = 0
  right = len(nums)

  while (left < right):
    mid = (left + right) // 2

    if (nums[mid] == target):
      return mid
    elif (nums[mid] < target):
      left = mid + 1
    else:
      right = mid

    # Post-processing
    # End Condition: left == right
    if (left != len(nums) and nums[left] == target):
      return left

    return -1
```

* Key Attributes:
  * An advanced way to implement binary search
  * Search conditions needs to access element's immediate right neighbor
  * Use element's right neighbor to determine if condition is met and decide
  whether to go left or right
  * Guarantees Search Space is at least 2 in size of each step
  * Post-processing required. Loop/Recursion ends when you have 1 element left.
  Need to assess if the remaining element meets the condition

* Distinguishing Syntax
  * Initial condition: ```left = 0, right = length```
  * Termination: ```left == right```
  * Searching Left: ```right = mid```
  * Searching Right: ```left = mid + 1```
