from fibonacci import recursive_fib
from subset_sum import isSubsetSum

import pytest

def test_fibonacci():
    assert recursive_fib(0) == 0
    assert recursive_fib(1) == 1
    assert recursive_fib(2) == 1
    assert recursive_fib(3) == 2
    assert recursive_fib(4) == 3
    assert recursive_fib(5) == 5
    assert recursive_fib(10) == 55

def test_subset_sum():
    nums = [3, 34, 4, 12, 5, 2]
    i = 9
    j = 78
    n = len(nums)
    assert isSubsetSum(nums, n, i) == True
    assert isSubsetSum(nums, n, j) == False
