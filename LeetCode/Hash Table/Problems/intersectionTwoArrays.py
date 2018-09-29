# Problem Description: Given two arrays, write a function to compute their intersection.

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert nums1 and nums2 to sets
        a = set(nums1)
        b = set(nums2)
        c = []

        # Iterate through List A and check if an element in List A is in List B
        for i in a:
            if (i in b):
                c.append(i)

        return c
