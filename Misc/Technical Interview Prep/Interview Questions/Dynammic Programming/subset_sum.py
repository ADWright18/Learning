def isSubsetSum(nums, n, sum):
    """
    Test if a subset of the given set has
    a sum equal to the given sum

    Parameters
    ----------
    nums : List[int]
        set of non-negative integers
    n : int
        length of the array/list
    sum : int
        target sum value

    Return
    ------
    bool
        True if there is a subset, False otherwise.
    """
    # Base Cases
    if (sum == 0):
        return True
    elif (n == 0 and sum != 0):
        return False

    # Ignore the last element if it is greater than sum
    if (nums[n-1] > sum):
        return isSubsetSum(nums, n-1, sum)

    # (a) Include the last element
    # (b) Exclude the last element
    return isSubsetSum(nums, n-1, sum-nums[n-1]) or isSubsetSum(nums, n-1, sum)
