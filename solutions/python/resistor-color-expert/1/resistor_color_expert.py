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

UNITNAME = {
    "0": " ohms",
    "1": " kiloohms",
    "2": " megaohms",
    "3": " gigaohms",
}

TOL = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def color_code(color: str) -> str:
    return str(COLORS.get(color, ""))


def resistor_label(colors: str) -> str:
    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"
    multi_index = 0
    if len(colors) == 5:
        multi_index += 1

    nums = []
    rest, unit = 0, 0
    for index in range(2 + multi_index):
        nums.append(color_code(colors[index]))
    value = int("".join(nums))

    # convert zero num to unitname
    rest += COLORS.get(colors[-2], 0) % 3
    unit += COLORS.get(colors[-2], 0) // 3

    value = value * 10 ** rest
    if value >= 1000:
        value = value / 1000
        unit += 1

    return "".join([
        str(value) if value % 1 != 0 else str(int(value)),
        UNITNAME.get(str(unit)),
        " ±" + TOL.get(colors[-1])
    ])
