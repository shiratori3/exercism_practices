from math import log10, floor


NUMS = {
    1000: "M",
    900:  "CM",
    500:  "D",
    400:  "CD",
    100:  "C",
    90:   "XC",
    50:   "L",
    40:   "XL",
    10:   "X",
    9:    "IX",
    5:    "V",
    4:    "IV",
    1:    "I",
}


def roman(number: int) -> str:
    if number <= 0 or number >= 4000:
        raise ValueError("Invaild number, must between 1 and 3999")

    res = []
    while number > 0:
        lv = floor(log10(number))
        reminder = number // (10 ** lv)
        if number > 1000:
            res.append(NUMS.get(1000) * reminder)
        else:
            if reminder in (4, 9):
                res.append(NUMS.get(reminder * 10 ** lv))
            elif reminder >= 5:
                res.append(NUMS.get(10 ** lv * 5))
                res.append(NUMS.get(10 ** lv) * (reminder - 5))
            else:
                res.append(NUMS.get(10 ** lv) * reminder)

        number -= 10 ** lv * reminder

    return "".join(res)
