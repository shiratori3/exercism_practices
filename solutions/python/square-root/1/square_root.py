def square_root(number: int) -> float:
    if number <= 0 or number % 1 > 0:
        raise ValueError("Only positive integers are allowed")
    res = number / 2
    tolerance = 0.000000000000000001
    diff = abs(res ** 2 - number)

    while diff > tolerance:
        res -= diff / (2 * res)
        diff = abs(res ** 2 - number)
    return res
