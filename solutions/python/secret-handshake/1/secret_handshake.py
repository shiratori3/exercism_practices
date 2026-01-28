words = {
    "4": "wink",
    "3": "double blink",
    "2": "close your eyes",
    "1": "jump",
}


def commands(binary_str: str) -> list[str]:
    res = []
    for i in range(5):
        if i != 0 and int(binary_str[i]) == 1:
            res.append(words[str(i)])
    return res if int(binary_str[0]) else list(reversed(res))
