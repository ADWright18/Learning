"""
Problem Description:
    Given an array of integers and an integer k, find out whether there are two
    distinct indices i and j in the array such that nums[i] = nums[j] and the
    absolute difference between i and j is at most k

Example:
Input:
nums = [1,2,3,1], k = 3

Output:
true

Solution:
1. Initialize a dictionary to store {value : index} pairs
2. Iterate through the list
    - If a value is already in the dictionary, get the absolute difference of the indices
        - If the difference is greater than k, return true
    - Otherwise, add the {value, index} pair to the dictionary
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {} # Store the {value, index} pairs

        for i in range(len(nums)):
            if (nums[i] in d):
                if (i - d[nums[i]] <= k):
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i

        return False
