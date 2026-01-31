ANIMALS = {
    8: {
        "name": "horse",
    },
    7: {
        "name": "cow",
        "action": "I don't know how she swallowed a cow!",
    },
    6: {
        "name": "goat",
        "action": "Just opened her throat and swallowed a goat!",
    },
    5: {
        "name": "dog",
        "action": "What a hog, to swallow a dog!",
    },
    4: {
        "name": "cat",
        "action": "Imagine that, to swallow a cat!",
    },
    3: {
        "name": "bird",
        "action": "How absurd to swallow a bird!",
    },
    2: {
        "name": "spider",
        "action": "It wriggled and jiggled and tickled inside her.",
    },
    1: {
        "name": "fly",
    },
}


def recite(start_verse: int, end_verse: int) -> list[str]:
    res = []
    for i in range(start_verse, end_verse + 1):
        res.extend(song(i))
        res.append("")
    res.pop()
    return res


def song(index: int) -> list[str]:
    res = ["I know an old lady who swallowed a {}.".format(
        ANIMALS[index].get("name")
    )]
    if index < 8:
        if index > 1:
            res.append(ANIMALS[index].get("action"))
        while index > 1:
            # shallow
            res.append("She swallowed the {} to catch the {}.".format(
                ANIMALS[index].get("name"),
                ANIMALS[index - 1].get("name")
                if ANIMALS[index - 1].get("name") != "spider"
                else "spider that wriggled and jiggled and tickled inside her"
            ))
            index -= 1

        res.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        return res
    if index == 8:
        res.append("She's dead, of course!")
        return res
