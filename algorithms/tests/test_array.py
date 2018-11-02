from algorithms.arrays import is_unique, check_permutation

import pytest

def test_is_unique():
    s = "string"
    assert is_unique(s) == True

    s = "bob"
    assert is_unique(s) == False

def test_check_permutation():
    s1 = "george"
    s2 = "father"
    assert check_permutation(s1, s2) == False

    s1 = "east"
    s2 = "seat"
    assert check_permutation(s1, s2) == True
