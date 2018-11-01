def recursive_fib(n):
    """
    Returns the nth number in the Fibonacci sequence

    Computes the value of the nth number in the
    fibonacci sequence by using the following
    recurrence relation: F(n) = F(n-1) + F(n-2)

    Parameters
    ----------
    n : int
        value in the sequence

    Return
    ------
    res : int
        nth value in the sequence
    """
    # Store known fibonacci values
    memo = {0 : 0, 1 : 1}

    if (n in memo):
        return memo[n]

    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)
