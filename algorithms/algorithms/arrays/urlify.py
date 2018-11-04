def urlify(s):
    """
    Replaces spaces in a string with %20

    Search for whitespace characters in the string
    and replace them with "%20"

    Parameters
    ----------
    s : str
        string to urlify

    Return
    ------
    res : string
        modified string
    """
    res = s.replace(" ","%20")

    return res
