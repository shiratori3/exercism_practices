def rebase(input_base: int, digits: list[int], output_base: int):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    s_digits = "".join(map(str, digits))
    if any(True for d in s_digits if d == "-" or int(d) >= input_base):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    total = sum([int(digit) * pow(input_base, index)
                 for index, digit in enumerate(reversed(digits))])
    res = []
    while total >= output_base:
        res.append(total % output_base)
        total = total // output_base
    res.append(total)
    res.reverse()
    return res
