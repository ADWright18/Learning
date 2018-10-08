"""
Problem Description:
    Given a sorted (in ascending order) integer array nums of n elements and a
    target value, write a function to search targe in nums. If target exists,
    then return its index, otherwise return -1.

Example
Input:
nums = [-1,0,3,5,9,12], target = 9

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
