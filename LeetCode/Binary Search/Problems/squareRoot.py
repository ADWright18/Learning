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
        # Initialize right and left
        current = 0
        mid = x // 2

        # Try i*i and incremement until i*i is greater than or equal to x
        for i in range(mid):
            if (i*i <= x):
                current = i
            else:
                return current
