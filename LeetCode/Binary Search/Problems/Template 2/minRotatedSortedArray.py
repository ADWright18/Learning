"""
Problem Description:
    Suppose an array sorted in ascending order is rotated at some pivot point
    unknown to you beforehand. You are given a target value to search. If found
    in the array return its index, otherwise return -1. You may assume no
    duplicate exists in the array.

Example
Input:
nums = [4,5,6,7,0,1,2], target = 0

Output:
4
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize left and right
        l = 0
        r = len(nums) - 1

        # Binary Search
        while (l < r):
            m = (l + r) // 2

            if (nums[m] > nums[m+1]):
                return nums[m+1]
            elif (nums[m] > nums[r]):
                l = m + 1
            else:
                r = m

        return nums[l]
