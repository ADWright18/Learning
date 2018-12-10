from algorithms.dynammic_programming import min_coin_change

import pytest

def test_min_coin_change():
    coins = [9,6,5,1]
    target = 11

    assert min_coin_change(coins, target) == 2
