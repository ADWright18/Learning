"""
Problem Description:
    Suppose Andy and Doris want to choose a restaurant for dinner, and they both
    have a list of restaurants represented by strings. You need to help them find
    out their common interest with the least list index sum.

    Assumption: You could assume there always exists an answer

Example:
Input:
Andy - ["Shogun", "Tapioca Express", "Burger King", "KFC"]
Doris - ["KFC", "Shogun", "Burger King"]

Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0 + 1)

Solution:
1. Combine each list into a combined list
2. Initialize a dictionary to store (item, index sum) pairs
2. Create a set from the combined list (remove duplicate values)
3. For each item in the set, check if the item is in both lists
    - If the item is in both lists, add (item, index sum) to the dictionary
4. Return the key with the least value from the dictionary
"""
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        c = list1 + list2           # Combined List
        d = {}                      # Store (item, index sum) pairs
        s = set(combined_list)      # Remove duplicates from combined list

        """
        Iterate through the set (combined list) and identify common items
        If the items are in both lists - add (item, index value) to d
        """
        for item in s:
            if (item in list1 and item in list2):
                d[item] = list1.index(item) + list2.index(item)

        minIndexSum = [min(d, key=d.get)]

        """
        Check if there is a tie
        If there is a tie, append the items to the minIndexSum list
        """
        if (d[minIndexSum[0]] in d.values()):
            for item in d:
                if (d[item] == d[minIndexSum[0]] and item not in minIndexSum):
                    minIndexSum.append(item)

        return minIndexSum
