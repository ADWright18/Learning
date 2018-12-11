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
    # Initialize the table
    table = [0 for i in range(target + 1)]

    # Base Case
    table[0] = 0

    # Initialize result
    for i in range(1, len(table)):
        table[i] = sys.maxsize

    # Bottom-up DP: Find the minimum number of coins for
    # values less than the target
    for i in range(1, target + 1):
        for j in range(0, len(coins)):
            if (coins[j] <= i):
                sub_result = table[i - coins[j]]

                # Check for INT_MAX to avoid overflow and see if
                # results can be minimized
                if (sub_result != sys.maxsize and sub_result + 1 < table[i]):
                    table[i] = sub_result + 1

    if (table[target] > target):
        return -1
    else:
        return table[target]
