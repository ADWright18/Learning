"""
Problem Description
    Given a non-negative integer numRows, generate the first numRows of Pascal's
    triangle

Example
Input:
5

Output:
[
[1],
[1,1],
[1,2,1],
[1,3,3,1],
[1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Initialize list of n (numRows) lists
        pascal = [[0] * n for n in range(1, numRows + 1)]

        for i in range(numRows):
            # Base Case
            if (i == 0):
                pascal[i][0] = 1

            # Other Base Case
            elif (i == 1):
                pascal[i][0] = 1
                pascal[i][1] = 1

            # Rows > 2
            else:
                pascal[i][0] = 1
                pascal[i][i] = 1

                # Fill in the values between 0 and i
                for j in range(1, i - 1):
                    print(pascal[i-1][j-1])
                    print(pascal[i-1][j])
                    pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

        return pascal
