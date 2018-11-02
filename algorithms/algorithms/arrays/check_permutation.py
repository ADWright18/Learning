def check_permutation(s1, s2):
    """
    Check if the given two strings are permutations
    of each other

    First, we'll check if the two strings are equal length.
    Then we'll store the characters of the first string in
    a list. If a character in the second string is not in
    the list, return False. Otherwise return True.

    Parameters:
    s1 : str
        first string
    s2 : str
        second string

    Return
    ------
    bool
        If the two strings are permutations, return True.
        Otherwise, return False
    """
    characters = []

    # Check if they are the same length
    if (len(s1) != len(s2)):
        return False

    for char in s1:
        characters.append(char)

    for char in s2:
        if (char in characters):
            characters.remove(char)
        else:
            return False

    return True
