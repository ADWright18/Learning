def is_one_away(s1, s2):
    """
    Checks if s1 and s2 are one edit distance away.

    Converts the given strings into a list of characters
    and checks if the difference between the two lists
    is at most 1

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
    
