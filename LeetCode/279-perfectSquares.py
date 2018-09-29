# Exercise 279: Perfect Squares

"""
Description: Given a positive integer n, find the least number of perfect square numbers which sum to n.

Related Problem: Finding the minimum # of coins that make a given value n

Recursive Solution:
1. Initialize a list of squares from 1 to n
2. Set result to infinity
3. Traverse through the squares list
    - If the square[i] <= n:
        - sub_result = minSquare(squareList, n - square[i])
        - If (sub_result != infinity and sub_result + 1 < res)
            - res = sub_result + 1
4. Return result


"""
