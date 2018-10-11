"""
Problem Description:
    We are playing the Guess Game. The game is as follows:
        - I pick a number 1 to n. You have to guess which number I picked.
        - Every time you guess wrong. I'll tell you whether the number is higher
        or lower
        - You call a pre-defined API "guess(int num)" which returns 3 possible
        results (-1, 1, or 0)

Example
Input:
n = 10, pick = 6

Output:
6
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize right and left
        l = 0
        r = n

        # Binary Search
        while (l <= r):
            # Choice will be the middle value
            choice = (l + r) // 2

            if (guess(choice) == 0):
                return choice

            # 1 if our choice is lower
            elif (guess(choice) == 1):
                l = choice + 1

            # -1 if out choice is higher
            elif (guess(choice) == -1):
                r = choice - 1

        return choice
