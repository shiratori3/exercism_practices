def is_paired(input_string: str) -> bool:
    inputlist = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in input_string:
        if char in pairs.values():
            inputlist.append(char)
        if char in pairs.keys():
            if not inputlist or inputlist.pop() != pairs[char]:
                return False
    # if len(inputlist):
    #     return False
    # return True
    return not inputlist
