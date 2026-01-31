from collections import Counter
from typing import List, Tuple, Optional


def can_chain(dominoes: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    if not dominoes:
        return []
    counts = Counter([num for pair in dominoes for num in pair])
    if not all(True for v in counts.values() if v % 2 == 0):
        return None

    found = find_longest([], dominoes, [], None)
    print(found)
    if not found:
        return None
    if len(found) != 1 and found[0][0] not in found[-1]:
        return None
    if len(found) == 1 and found[0][0] != found[0][1]:
        return None

    return found


def find_longest(
    longest: List[Tuple[int, int]],
    search: List[Tuple[int, int]],
    link: List[Tuple[int, int]],
    right: Optional[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    searched = search.copy()
    linked = link.copy()
    # init
    if right is None:
        first = searched[0]
        linked.append(first)
        searched.remove(first)
        return find_longest(
            longest,
            search[1:],
            [first],
            first
        )
    # finished
    if not search:
        if len(longest) < len(link):
            return link.copy()
        return longest

    for i, tup in enumerate(search):
        a, b = tup
        r = right[1]

        if a == r:
            new = find_longest(
                longest,
                search[:i] + search[i+1:],
                link + [tup],
                tup
            )
            if len(new) > len(longest):
                longest = new
        elif b == r:
            flipped = (b, a)
            new = find_longest(
                longest,
                search[:i] + search[i+1:],
                link + [flipped],
                flipped
            )
            if len(new) > len(longest):
                longest = new
    return longest
