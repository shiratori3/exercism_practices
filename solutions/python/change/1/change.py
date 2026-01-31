from math import gcd, inf
from functools import reduce


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    coins_avail = [_ for _ in reversed(coins) if target >= _]
    coins_avail_list = [list(coins_avail[i-1:])
                        for i in range(len(coins_avail), 0, -1)]

    min_len = inf
    min_res = []
    for cur_coins in coins_avail_list:
        rest = target
        res = []
        for index, coin in enumerate(cur_coins):
            if rest >= coin:
                for v in range(rest // coin, 0, -1):
                    if not (rest - coin * v):
                        res.extend([coin] * v)
                        rest = 0
                        break
                    # rest should be sum of a*x + b*y ... + c*z
                    if not can_sum(rest - coin * v,  cur_coins[index + 1:]):
                        continue
                    res.extend([coin] * v)
                    rest = rest - coin * v
        if rest == 0 and len(res) < min_len:
            min_len = len(res)
            min_res = res
    if not min_res:
        raise ValueError("can't make target with given coins")
    else:
        return sorted(min_res)


def can_sum(a, nums):
    if not nums or a <= 0:
        return False

    g = reduce(gcd, nums)
    if a % g != 0:
        return False

    # close faster
    a //= g
    nums = [n // g for n in nums]

    dp = [False] * (a + 1)
    dp[0] = True
    for num in nums:
        for i in range(num, a + 1):
            if dp[i - num]:
                dp[i] = True
    return dp[a]