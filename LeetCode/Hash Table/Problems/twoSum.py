"""
Problem Desciption: Given an array of integers, return indices of the two numbers
such that they add up to a specific target. You may assume that each input would
have exactly one solution, and you may not use the same element twice.

Solution:
1. Initialize a hash map to store the value (key) and the index (value)
2. Iterate through the nums list to add the (value, index) pairs to the hash map
    - The value will be a list of the indices that contain the value in the nums list
    - Example: nums = [3,3,4,5,2] -> {3 : [0,1]}
3. Iterate through the hashmap - for j in hash map
    - Calculate k = target - j
    - Check if k exists in the hash map
    - Check if k is equal to j

"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hashmap = {}

        for i in range(len(nums)):
            if (nums[i] in hashmap):
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]

        for j in hashmap:
            k = target - j
            if (k == j and len(hashmap[j]) > 1):
                return [hashmap[j][0], hashmap[j][1]]
            elif (k in hashmap):
                return [hashmap[j][0], hashmap[k][0]]
