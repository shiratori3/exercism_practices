from collections import Counter
from string import ascii_lowercase


def is_isogram(string: str) -> bool:
    return all([True if ((char in ascii_lowercase and num == 1) or
                         char not in ascii_lowercase)
                else False for char, num in Counter(string.lower()).items()])
