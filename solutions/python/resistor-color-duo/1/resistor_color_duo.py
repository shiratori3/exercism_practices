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


def value(colors: list[str]) -> int:
    return int("".join([color_code(color) if index <= 1 else ""
                        for index, color in enumerate(colors)]))
