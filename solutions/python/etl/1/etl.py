from typing import Dict, List


def transform(legacy_data: Dict[int, List[str]]) -> Dict[str, int]:
    res = {}
    for v, chars in legacy_data.items():
        for char in chars:
            res.setdefault(char.lower(), v)
    return res
