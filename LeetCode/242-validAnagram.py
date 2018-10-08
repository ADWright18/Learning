"""
Problem Description:
    Given two strings s and t, write a function to determine if t is an anagram
    of s

Example
Input:
s = "anagram", t = "nagaram"

Output:
true
"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Create a list of characters for each string
        s_list = list(s)
        t_list = list(t)

        # Sort both lists and compare
        if (sorted(s_list) == sorted(t_list)):
            return True
        else:
            return False
