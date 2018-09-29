# Problem Description: Find the Happy Number

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Initialize Set
        s = set()
        cycle = False

        while (cycle != True):

            value = 0

            # Seperate n into list of digits
            digits = [int(d) for d in str(n)]

            # Return the sum of the digits squared
            for i in digits:
                value += i**2

            if (value == 1):
                return True
            elif (value in s):
                cycle = True
            else:
                s.add(value)
                n = value

        return False
