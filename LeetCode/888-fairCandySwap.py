# Exercise 888: Fair Candy Swap

"""
Steps:
1. Find the sum of each list
2. Find the delta (difference) between each list

sumA - sumB = delta

3. Solve the following equation:

sumA - candy_A + candy_B = sumB - candy_B + candy_A
sumA - sumB = 2(candy_A + candy_B) = delta
candy_B = candy_A - delta/2

4. Iterate through A until an item in B satisfies -> candy_B = candy_A - delta/2
5. Return[candy_A, candy_B]
"""

class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA = sum(A)
        sumB = sum(B)
        setA = set(A)
        setB = set(B)
        delta = sumA - sumB

        for i in setA:
            j = i - float(delta/2)
            if j in setB:
                return [i, int(j)]
