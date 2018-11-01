def is_unique(s):
    """
    Check if the string contains only unique characters

    Each unique character is stored in list. If a character
    is already in the list, return False. Otherwise, return
    True.

    Parameters
    ----------
    s : str
        input string

    Return
    ------
    bool
        True if there are only unique characters, False otherwise.
    """
    seen = []

    for char in s:
        if (char not in seen):
            seen.append(char)
        else:
            return False

    return True
