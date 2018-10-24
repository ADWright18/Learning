class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Strip punctuation
        for p in string.punctuation:
            s = s.replace(p, "")

        # Strip whitespace
        s = s.replace(" ", "")

        # Make all letters lowercase
        s = s.lower()

        # Store the length - 1 (for convenience)
        n = len(s) - 1

        # Check if the string has an odd or even number of characters
        # If odd -> exclude middle character
        if (n % 2 == 1):

            # Find the middle index (character)
            m = n // 2

            for i in range(len(s)):
                if (i == m):
                    continue
                elif (s[i] != s[n-i]):
                    return False
        elif (n % 2 == 0):
            for i in range(len(s)):
                if (s[i] != s[n-i]):
                    return False

        return True
