def is_one_away(s1, s2):
    """
    Checks if s1 and s2 are one edit distance away.

    Converts the given strings into a list of characters
    and checks if the intersection of s1 and s2 are one
    away from the length of both s1 and s2

    Parameters
    ----------
    s1 : str
        first input string
    s2 : str
        second input string

    Return
    ------
    bool
        If the edit distance is at most 1, return True.
        Otherwise, return False
    """
    # Create a list of characters for each string
    a = list(s1)
    b = list(s2)
    c = a + b

    # Store the intersection of a and b
    d = []

    # Combine the lists
    # If a character is in both a and b, remove that character from a and b
    for i in c:
        if (i in a and i in b):
            d.append(i)
            a.remove(i)
            b.remove(i)

    # Check if the length of s1 and s2 are at most one away from the
    # length of the intersection
    if (len(s1) > len(d) + 1 or len(s1) < len(d) - 1):
        return False

    if (len(s2) > len(d) + 1 or len(s2) < len(d) - 1):
        return False

    return True
