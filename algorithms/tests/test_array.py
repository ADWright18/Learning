from algorithms.arrays import (
    is_unique,
    check_permutation,
    urlify,
    is_palindrome_permutation
    )

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

def test_urlify():
    s = "this is a test"
    assert urlify(s) == "this%20is%20a%20test"

    s = " "
    assert urlify(s) == "%20"

def test_is_palindrome_permutation():
    s = "tact coa"
    assert is_palindrome_permutation(s) == True

    s = "test"
    assert is_palindrome_permutation(s) == False

    s = "DCODEME E MEDOC D"
    assert is_palindrome_permutation(s) == True

    s = " "
    assert is_palindrome_permutation(s) == True
