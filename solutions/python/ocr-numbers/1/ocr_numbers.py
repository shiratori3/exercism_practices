NUMS = {
    " _ | ||_|   ": "0",
    "     |  |   ": "1",
    " _  _||_    ": "2",
    " _  _| _|   ": "3",
    "   |_|  |   ": "4",
    " _ |_  _|   ": "5",
    " _ |_ |_|   ": "6",
    " _   |  |   ": "7",
    " _ |_||_|   ": "8",
    " _ |_| _|   ": "9",
}


def convert(input_grid: list[str]) -> str:
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    if any(True if len(_) % 3 != 0 else False for _ in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    nums = []
    for y in range(0, len(input_grid), 4):
        for x in range(0, len(input_grid[y]), 3):
            num = [line[x:x+3] for line in input_grid[y:y+4]]
            nums.append(NUMS.get("".join(num), "?"))
        nums.append(",")
    nums.pop()
    return "".join(nums)




