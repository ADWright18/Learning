"""
Problem Description:
    A peak element is an element that is greater than its neighbors. Given an
    input array nums, where nums[i] =/= nums[i+1], find a peak element and
    return its index. The array may contain multiple peaks, in that case return
    the index to any one of the peaks is fine.

Example
Input:
nums = [1,2,3,1]

Output:
2
"""
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize right and left
        l = 0
        r = len(nums) - 1

        # Binary Search
        while (l < r):
            m = (l + r) // 2

            if (nums[m] < nums[m+1]):
                l = m + 1
            elif (nums[m] > nums[m+1]):
                r = m

        return l

        if (l != len(nums)):
            if (nums[m] > nums[m-1] and nums[m] > nums[m+1]):
                return m
        return -1
