def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0 or number % 1 > 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    divisors = {1}
    n = 2
    while n * n <= number:
        if number % n == 0:
            divisors.add(n)
            if n != number // n:
                divisors.add(number // n)
        n += 1

    return "perfect" if number == sum(divisors) \
        else "abundant" if number < sum(divisors) \
        else "deficient"
