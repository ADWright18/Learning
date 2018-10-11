"""
Problem Description:
    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to you beforehand. You are given a target value to search. If found in the
    array return its index, otherwise return -1. You may assume no dupliacte
    exists in the array. Your algorithm's runtime complexity must be in the order
    of O(log n)

Example
Input:
nums = [4,5,6,7,0,1,2], target = 0

Output:
4
"""
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize list for sorted nums
        sorted_nums = nums

        for i in range(len(nums) - 1):
            if (nums[i] > nums[i + 1]):
                sorted_nums = nums[i + 1: len(nums)] + nums[: i + 1]

        # Initialize right and left
        l = 0
        r = len(nums) - 1

        # Binary Search
        while (l <= r):
            m = (l + r) // 2

            if (sorted_nums[m] == target):
                return nums.index(sorted_nums[m])
            elif (sorted_nums[m] > target):
                r = m - 1
            elif (sorted_nums[m] < target):
                l = m + 1

        return -1
