from typing import List, Optional


def triplets_with_sum(number: int) -> List[Optional[List[int]]]:
    res = set()
    for a in range(1, number // 3):
        for b in range(a + 1, (number - a) // 2 + 1):
            c = number - a - b
            if c <= b:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                res.add((a, b, c))
    return [list(t) for t in sorted(res)]
