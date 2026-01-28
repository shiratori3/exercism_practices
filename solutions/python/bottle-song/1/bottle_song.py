nums = {
    0: "no",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
}


def song(num: int):
    return [
        "{0} green bottle{1} hanging on the wall,".format(
            nums.get(num).title(), "s" if num != 1 else ""),
        "{0} green bottle{1} hanging on the wall,".format(
            nums.get(num).title(), "s" if num != 1 else ""),
        "And if one green bottle should accidentally fall,",
        "There'll be {0} green bottle{1} hanging on the wall.".format(
            nums.get(num-1), "s" if num - 1 != 1 else "")
    ]


def recite(start: int, take=1) -> list[str]:
    res = []
    for i in range(take):
        if i > 0:
            res.append("")
        res.extend(song(start - i))
    return res
