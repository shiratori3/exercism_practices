def is_valid(isbn: str) -> bool:
    num_s = "".join(isbn.split("-"))
    if len(num_s) != 10:
        return False
    total = 0
    for index, v in enumerate(reversed(num_s)):
        if v not in "0123456789X":
            return False
        if v == "X" and index != 0:
            return False
        total += 10 * (index + 1) if v == "X" else int(v) * (index + 1)
    return total % 11 == 0
