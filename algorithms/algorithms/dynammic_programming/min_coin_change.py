import sys

def min_coin_change(coins, target):
    """
    Return minimum number of coins to reach the target

    Parameters
    ----------
    coins : List[int]
        list of coin denominations
    target : int
        target value

    Return
    ------
    int
        If the target value can be reached with the given
        coin denominations, return the minimum number of
        coins to reach the target. Otherwise, return -1
    
    """
    # Base Case
    if (target == 0):
        return 0

    # Initialize result
    result = sys.maxsize

    # Try every coin that has smaller value than target
    for i in range(0, len(coins)):
        if (coins[i] <= target):
            sub_result = min_coin_change(coins, target - coins[i])

            # Check for INT_MAX to avoid overflow and see if
            # results can be minimized
            if (sub_result != sys.maxsize and sub_result + 1 < result):
                result = sub_result + 1

    return result
