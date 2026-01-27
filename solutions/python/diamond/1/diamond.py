from string import ascii_uppercase


def rows(letter: str) -> list[str]:
    n = ascii_uppercase.find(letter)
    max_width = n * 2 + 1
    res = []
    for i in range(n+1):
        char = ascii_uppercase[i]
        t = char + " " * (2 * i - 1) + char if i > 0 else char
        res.append(t.center(max_width, " "))
    return res + res[n-1::-1] if letter != "A" else res
