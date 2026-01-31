from collections import Counter
from typing import Dict


def count_words(sentence: str) -> Dict[str, int]:
    words = [word.lower().strip(".,':!&@$%^&") for word in sentence.split()]
    # remove blank item ""
    words = [w for w in words if w]
    if len(words) == 1:
        temp = " ".join(words).replace("_", " ").replace(",", " ")
        words = [word for word in temp.split()]
    return dict(Counter(words))
