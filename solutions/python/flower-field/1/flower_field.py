def annotate(garden: list[str]) -> list[str]:
    if not garden:
        return []
    if garden[0] == "":
        return garden
    row, col = len(garden), len(garden[0])
    if not all([False if len(garden[i]) != col else True for i in range(row)]):
        raise ValueError("The board is invalid with current input.")
    if len("".join(garden).replace("*", "").strip()) > 0:
        raise ValueError("The board is invalid with current input.")

    garden_num = [0 if i == " " else "_" for _ in garden for i in list(_)]
    # fill num around the flower
    i = fill_num(garden_num, row, col)
    while i:
        i = fill_num(garden_num, row, col)
    return ["".join(list(map(str, garden_num[i:i+col]))).replace("0", " ")
            for i in range(0, row * col, col)]


def fill_num(garden_num: list[int | str], row: int, col: int) -> bool:
    try:
        index = garden_num.index("_")
        if index != -1:
            garden_num[index] = "*"
            x, y = index % col, index // col
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < col and 0 <= ny < row:
                        if garden_num[ny * col + nx] not in ("*", "_"):
                            garden_num[ny * col + nx] += 1
            return True
    except ValueError:
        return False
