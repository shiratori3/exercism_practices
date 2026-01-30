LYRICS = {
    12: "twelve Drummers Drumming, ",
    11: "eleven Pipers Piping, ",
    10: "ten Lords-a-Leaping, ",
    9:  "nine Ladies Dancing, ",
    8:  "eight Maids-a-Milking, ",
    7:  "seven Swans-a-Swimming, ",
    6:  "six Geese-a-Laying, ",
    5:  "five Gold Rings, ",
    4:  "four Calling Birds, ",
    3:  "three French Hens, ",
    2:  "two Turtle Doves, ",
    1:  "and a Partridge in a Pear Tree.",
    0:  "a Partridge in a Pear Tree.",
}

NUMS = {
    12: "twelfth",
    11: "eleventh",
    10: "tenth",
    9:  "ninth",
    8:  "eighth",
    7:  "seventh",
    6:  "sixth",
    5:  "fifth",
    4:  "fourth",
    3:  "third",
    2:  "second",
    1:  "first",
}


def song(line: int) -> list[str]:
    res = ["On the {0} day of Christmas my true love gave to me: ".format(NUMS[line])]
    if line == 1:
        lines = [LYRICS[index] for index in range(line)]
    else:
        lines = [LYRICS[index + 1] for index in range(line)]
    res.extend(reversed(lines))
    return ["".join(res)]


def recite(start_verse: int, end_verse: int) -> list[str]:
    if start_verse == end_verse:
        res = song(start_verse)
        return res
    res = []
    for index in range(end_verse - start_verse + 1):
        res.append(recite(start_verse + index, start_verse + index)[0])
    return res
