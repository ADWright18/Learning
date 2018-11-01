from algorithms.arrays import is_unique

import pytest

def test_is_unique():
    s = "string"
    assert is_unique(s) == True

    s = "bob"
    assert is_unique(s) == False
