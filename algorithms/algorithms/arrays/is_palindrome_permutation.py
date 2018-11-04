def is_palindrome_permutation(s):
    """
    Check if a string is a permutation of a palindrome

    Parameters
    ----------
    s : str
        input string

    Return
    ------
    bool
        If the string is a palindrome permutation, return
        True. Otherwise, return False
    """
    # Remove whitespace
    s1 = s.replace(" ","")
    s1 = s1.lower()

    # Dictionary to store the occurrence of each character
    d = {}
    middle = ""

    for char in s1:
        if (char not in d):
            d[char] = 1
        else:
            d[char] += 1

    # Check the character occurrences
    for key in d:
        if (d[key] % 2 == 1):
            if (middle == ""):
                middle = middle + key
            else:
                return False

    return True
