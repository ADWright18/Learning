"""
Problem Description: Given two strings s and t, determine if they are isomorphic.

Solution:
1. Initialize a dictionary
2. Iterate through string s
    - If s[i] is in the dictionary and d[s[i]] is not equal to t[i] - Return False
    - If t[i] is a value in the dictionary - Return False
    - Otherwise, d[s[i]] = t[i]
3. Return True
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            elif t[i] in d.values(): # Check if t[i] is already mapped to a key
                return False
            else:                    # Add (s[i], t[i]) to the dictionary
                d[s[i]] = t[i]
        return True
