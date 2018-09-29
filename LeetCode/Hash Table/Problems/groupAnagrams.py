"""
Problem Description: Given an array of strings, group anagrams together

Example:
Input:
["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]

Solution:
1. Initialize a dictionary to store {sorted_char : [list of anagrams]} pairs
2. Iterate through the list of words
    - If sorted(word) is already in the dictionary, d[sorted_char].append(word)
    - Otherwise, add {sorted(word) : word} to the dictionary
3. Return d.values()
"""
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {} # Store {sorted(word) : [list of anagrams]} pairs

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if (sorted_word in d):
                d[sorted_word].append(word)
            else:
                d[sorted_word] = [word]

        v = list(d.values())
        return v
