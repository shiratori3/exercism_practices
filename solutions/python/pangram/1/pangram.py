from collections import Counter
from string import ascii_lowercase


def is_pangram(sentence: str) -> bool:
    return ascii_lowercase in "".join(sorted(Counter(sentence.lower()).keys()))
