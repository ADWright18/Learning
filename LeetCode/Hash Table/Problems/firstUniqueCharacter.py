"""
Problem Description:
    Given a string, find the first non-repeating character in it and return it's
    index. If it doesn't exist, return -1.

Example:
Input:
s = "leetcode"

Output:
return 2

Solution:
1. Initialize a dictionary to store {char : index} pairs
2. Iterate through each char in the string
    - If the char is already in the dictionary, remove it
    - Otherwise, add the {char : index} pair to the dictionary
3. If the dictionary is empty, then there are no non-repeating characters
    - Otherwise, return the minimum value of the dictionary
"""
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {} # Store unique characters of the list
        a = [] # Store duplicate characters

        for i in range(len(s)):
            if (s[i] in d):
                a.append(s[i])
                del d[s[i]]
            elif (s[i] not in d and s[i] not in a):
                d[s[i]] = i

        # Check if d is empty
        if (not bool(d)):
            return -1
        else:
            return min(d.values())
