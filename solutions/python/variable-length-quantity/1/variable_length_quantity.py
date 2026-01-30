def encode(numbers: list[bytes]):
    res = []
    for num in numbers:
        bytes_ = []
        while True:
            b = num & 0x7F
            num >>= 7
            if bytes_:
                b |= 0x80
            bytes_.insert(0, b)
            if num == 0:
                break
        res.extend(bytes_)
    return res


def decode(bytes_: list[bytes]):
    res = []
    cur = 0
    for b in bytes_:
        cur = (cur << 7) | (b & 0x7F)
        if b & 0x80 == 0:
            res.append(cur)
            cur = 0
    if bytes_ and (bytes_[-1] & 0x80):
        raise ValueError("incomplete sequence")
    return res
