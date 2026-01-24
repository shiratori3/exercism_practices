def is_paired(input_string: str) -> bool:
    inputlist = []
    mapdict = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in input_string:
        if char in "[{(":
            inputlist.append(char)
        if char in ")}]":
            try:
                c = inputlist.pop()
                if c != mapdict[char]:
                    return False
            except IndexError:
                return False
    if len(inputlist):
        return False
    return True
