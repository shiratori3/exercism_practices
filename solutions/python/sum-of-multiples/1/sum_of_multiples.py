from typing import List


def sum_of_multiples(limit: int, multiples: List[int]) -> int:
    res = set()
    for num in multiples:
        if num:
            for i in range(0, limit, num):
                res.add(i)
    return sum(res)
