def square(number: int) -> int:
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    return sum([2 ** i for i in range(64)])
