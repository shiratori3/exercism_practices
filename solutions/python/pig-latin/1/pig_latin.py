def translate(text: str) -> str:
    if " " in text:
        res = []
        for word in text.split(" "):
            res.append(translate(word))
        return " ".join(res)

    if text[0] in "aeiou" or text.startswith(("xr", "yt")):
        return text + "ay"

    # qu
    index_qu = text.find("qu")
    if index_qu >= 0:
        if not find_vowels(text[:index_qu+1]):
            return text[index_qu+2:] + text[:index_qu+2] + "ay"
    # y
    index_y = text.find("y", 1)
    if index_y >= 0:
        if not find_vowels(text[:index_y]):
            return text[index_y:] + text[:index_y] + "ay"
    # others
    if find_vowels(text):
        index_vowel = min(i for i, char in enumerate(text) if char in "aeiou")
        return text[index_vowel:] + text[:index_vowel] + "ay"
    else:
        return text + "ay"


def find_vowels(text: str) -> bool:
    return any(True for char in text if char in "aeiou")