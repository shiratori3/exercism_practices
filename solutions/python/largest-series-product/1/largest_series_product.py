from functools import reduce


def largest_product(series: str, size: int) -> int:
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if not series.isnumeric():
        raise ValueError("digits input must only contain digits")

    max = 0
    for index in range(len(series) - size + 1):
        res = reduce(lambda x, y: x * y, list(map(int,
                                                  series[index:index + size])))
        max = res if res > max else max

    return max
