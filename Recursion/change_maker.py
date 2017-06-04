"""from udemy course

Given a target amount n and a list (array) of distinct coin values, what's the fewest coins needed to make the change amount.
For example:
If n = 10 and coins = [1,5,10] -> 1
"""


def rec_coin(target, coins):

    biggest_usable_coin = 0

    for c in coins:
        if c == target:
            return 1
        if c < target:
            biggest_usable_coin = c
        else:
            break

    target = target - biggest_usable_coin
    #i = coins.index(biggest_usable_coin)  # no help - already breaking out of loop
    #coins = coins[:i]

    num_coins = 1 + rec_coin(target, coins)

    return num_coins

coins = [1, 5, 10, 25]
print rec_coin(74, coins), "should be: 8"
print rec_coin(23, coins), "should be: 5"
print rec_coin(45, coins), "should be: 3"
