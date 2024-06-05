#!/usr/bin/python3
"""
    Making change module
"""


def makeChange(coins, total):
    """
        determines the fewest number
        of coins needed to meet a
        given amount total given a pile of coins
    """
    if total <= 0:
        return 0
    remai = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remai > 0:
        if coin_idx >= n:
            return -1
        if remai - sorted_coins[coin_idx] >= 0:
            remai -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
