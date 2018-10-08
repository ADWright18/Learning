"""
Problem Description:
    Given a non-empty array of integers, return the k most frequent elements

Example
Input:
nums = [1,1,1,2,2,3], k = 2

Output:
[1,2]
"""
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Initialize dictionary to store {value : occurrences} pairs
        d = {}
        res = []

        # Input the unique values of the list
        for i in set(nums):
            d[i] = 0

        # Iterate through the "nums" list to count the occurrences
        for i in nums:
            d[i] += 1

        # Return the k most frequent elements
        while (k > 0):
            key = max(d, key=d.get)
            d.pop(key)

            # Iterate k
            k = k - 1

            # Append key to result list
            res.append(key)

        return res
