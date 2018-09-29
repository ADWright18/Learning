"""
Problem Description: Given two arrays, write a function to compute their intersection

Example:
Input:
nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]

Output:
[4, 9]

Solution:
1. Initialize a dictionary and a list to store the intersecting values
2. Iterate through the list and add {value : occurrences} pair to the dictionary
    - Increment the occurrences when a value is encountered
3. Iterate through the second list
    - If the value is in the dictionary, decrement the occurrences and add the
    value to the list
4. Return the list
"""
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {} # Store {value : occurences} for a list
        a = [] # Store the intersecting values

        for i in nums1:
            if (i in d):
                d[i] += 1
            else:
                d[i] = 1

        for j in nums2:
            if (j in d and d[j] != 0):
                a.append(j)
                d[j] -= 1

        return a
