def steps(number: int) -> int:
    if number <= 0 or number % 1 > 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while number > 1:
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        step += 1
    return step
