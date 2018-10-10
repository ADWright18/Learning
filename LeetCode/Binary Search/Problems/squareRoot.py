"""
Problem Description:
    Compute and return the square root of x, where x is guarenteed to be a
    non-negative integer. Since the return type is an integer, the decimal
    digits are truncated and only the integer part of the result is returned

Example
Input:
4

Output:
2
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Base case
        if (x == 0 or x == 1):
            return x

        # Store the res if m*m < x
        res = 0

        # Initialize right and left
        r = x
        l = 0

        # Binary Search
        while (l <= r):
            m = (l + r) // 2

            if (m*m == x):
                return m
            elif (m*m < x):
                l = m + 1
                res = m
            elif (m*m > x):
                r = m - 1

        return res
