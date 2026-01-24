def rebase(input_base: int, digits: list[int], output_base: int):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(True for d in digits if d >= input_base or d < 0):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    total = sum([digit * pow(input_base, index)
                 for index, digit in enumerate(digits[::-1])])
    res = []
    while total >= output_base:
        res.append(total % output_base)
        total = total // output_base
    res.append(total)
    res.reverse()
    return res
