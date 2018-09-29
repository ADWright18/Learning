# Problem Desciption: Given a non-empty of integers, every element appears twice except for one. Find that single one

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset = set(nums)

        # Remove the elements that are in the hashset from the nums list
        for i in hashset:
            nums.remove(i)

        # Remove the remaining elements (duplicates) in the nums list from the hashset
        for j in nums:
            hashset.remove(j)

        # Return the last character from the hashset (the single number)
        for x in hashset:
            return x
