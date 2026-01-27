def answer(question: str) -> int | None:
    q_string = question.rstrip("?").split(" ")
    op = {
        "plus": "+",
        "minus": "-",
        "multiplied": "*",
        "divided": "/"
    }
    temp, res = [], 0
    for char in q_string:
        if char in ["cubed"]:
            raise ValueError("unknown operation")
        if is_num(char):
            if temp and is_num(temp[-1]):
                raise ValueError("syntax error")
            temp.append(char)
        if char in op.keys():
            if temp and temp[-1] in op.values():
                raise ValueError("syntax error")
            temp.append(op[char])
        if len(temp) == 3:
            t = eval("".join(temp))
            temp = []
            temp.append(str(t))

    if len(temp) % 2 == 0:
        raise ValueError("syntax error")
    return float(temp[0])


def is_num(char: str) -> bool:
    try:
        float(char)
        return True
    except ValueError:
        return False