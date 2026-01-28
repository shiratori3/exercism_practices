
COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def color_code(color: str) -> str:
    return str(COLORS.get(color, ""))


def label(colors: list[str]) -> str:
    res = []
    rest, unit = 0, 0
    for index, color in enumerate(colors):
        v = color_code(color)
        if index == 0 and v == "0":
            continue
        if index <= 1:
            res.append(v)
        if index == 2:
            # convert zero num to unitname
            rest += COLORS.get(color, 0) % 3
            unit += COLORS.get(color, 0) // 3
            if rest == 2 and res[-1] == "0":
                res.pop()
                unit += 1
                rest = 0
    if unit == 0:
        unit_name = " ohms"
    elif unit == 1:
        unit_name = " kiloohms"
    elif unit == 2:
        unit_name = " megaohms"
    elif unit == 3:
        unit_name = " gigaohms"
    res.append("".join([" " if rest == 0 else str(10 ** rest), unit_name])[1:])
    return "".join(res)
