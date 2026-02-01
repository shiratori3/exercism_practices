from typing import List


def proverb(*args, **kwargs) -> List[str]:
    res = []
    if not args:
        return res
    qualifier = kwargs.get("qualifier", "")
    last = f"{qualifier} {args[0]}" if qualifier else args[0]
    for index, arg in enumerate(args):
        if index != len(args) - 1:
            res.append(f"For want of a {arg} the {args[index+1]} was lost.")
        if index == len(args) - 1:
            res.append(f"And all for the want of a {last}.")
    return res