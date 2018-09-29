"""
Problem Description:
    Given an array of size n, find the majority element. The majority element is
    the element that appears more than n/2 times

    Assumption - The array is non-empty and the majority element exist in the array

Example:
Input:
[3,2,3]

Output:
3

Solution:
1. Initialize a dictionary to store {value : occurrence} pairs
2. Iterate through the list and count the number of occurrences for each value
    - If the value is not in the dictionary, d[value] = 1
    - Otherwise, d[value] += 1
    - Return the a value if the number of occurrences > n/2
"""
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {} # Store {value : occurrences} pairs

        for i in range(len(nums)):

            if (nums[i] not in d):
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

            if (d[nums[i]] > len(nums)//2):
                return nums[i]
