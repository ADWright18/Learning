"""
Problem Description:
    Implement an algorithm to determine if a string has all unique characters.
    What is you cannot use additional data structures.

Example
Input:
s = dad

Output:
False
"""
# Solution #1
# Time Complexity -> O(1) + O(n) = O(n)
def isUnique(s):
    return (len(s) == len(set(s)))

# Solution #2 (No additional data structures)
# Time Complexity -> O(n^2) * O(1) = O(n^2)
def isUniqueChar(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if (s[i] == s[j] and i != j):
                return False

    return True

# Main Program
var1 = "dad"
print(isUnique(var1))

var2 = "father"
print(isUniqueChar(var2))
