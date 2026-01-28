from collections import Counter


def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    res = []
    word_counter = Counter(word.lower())
    for w in candidates:
        if word_counter == Counter(w.lower()):
            if w.lower() != word.lower() and w not in (res):
                res.append(w)
    return res
