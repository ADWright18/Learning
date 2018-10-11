"""
Problem Description:
    Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad. You are given
    an API bool isBadVersion(version) which will return whether "version" is bad.
    Implement a function to find the first bad version.

    Note: You should minimize the number of calls to the API

Example:
Given n = 5, and version = 4 is the first bad version

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize right and left
        l = 0
        r = n

        # Binary Search
        while (l < r):
            m = (l + r) // 2

            if (isBadVersion(m) == False and isBadVersion(m + 1) == True):
                return m + 1
            elif (isBadVersion(m) == True and isBadVersion(m + 1) == True):
                r = m
            elif (isBadVersion(m) == False and isBadVersion(m + 1) == False):
                l = m + 1

        if (l != n):
            if (isBadVersion(m) == False and isBadVersion(m + 1) == True):
                return m + 1

        return -1
