from math import floor


def prime(number: int) -> int:
    if number < 1:
        raise ValueError('there is no zeroth prime')
    cnt = 0
    generator = prime_generator()
    while True:
        res = next(generator)
        cnt += 1
        if cnt == number:
            return res


def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
