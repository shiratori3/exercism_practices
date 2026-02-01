from typing import List


def primes(limit: int) -> List[int]:
    dp = [True for _ in range(limit + 1)]
    if limit < 2:
        return []
    # 0, 1 not count
    dp[0], dp[1] = False, False
    for num in range(2, limit):
        for v in range(num + num, limit + 1, num):
            dp[v] = False
    return [index for index, v in enumerate(dp) if v]
