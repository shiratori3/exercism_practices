def transpose(text: str) -> str:
    if not text:
        return text

    lines = text.split("\n")
    max_width = max(len(_) for _ in lines)

    res = [[] for _ in range(max_width)]
    widths = [[[] for _ in range(len(lines))] for _ in range(max_width)]
    for h, l in enumerate(lines):
        width = len(l)
        for w, char in enumerate(l.ljust(max_width, " ")):
            res[w].append(char)
            widths[w][h] = False
            if w > width - 1:
                widths[w][h] = True
    for index in range(max_width):
        word = ""
        if not any(widths[index]):
            word = "".join(res[index])
        else:
            # take first False to Last False
            # [False, True, False, True] should return 2
            last = len(widths[index]) - 1 - widths[index][::-1].index(False)
            word = "".join(res[index][:last+1])
        res[index] = word
    return "\n".join(res)
