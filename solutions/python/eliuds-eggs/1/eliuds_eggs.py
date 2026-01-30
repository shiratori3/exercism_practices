def egg_count(display_value: int) -> int:
    cnt = 0
    while display_value > 0:
        if display_value & 0x1:
            cnt += 1
        display_value >>= 1
    return cnt
