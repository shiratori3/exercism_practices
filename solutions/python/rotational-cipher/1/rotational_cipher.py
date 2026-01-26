from string import ascii_lowercase, ascii_uppercase


def rotate(text: str, key: int) -> str:
    return "".join([ascii_lowercase[(ascii_lowercase.find(c) + key) % 26]
                    if c in ascii_lowercase
                    else ascii_uppercase[(ascii_uppercase.find(c) + key) % 26]
                    if c in ascii_uppercase
                    else c for c in text])
    # org, res = [], []
    # for c in text:
    #     if c in ascii_letters:
    #         if c in ascii_lowercase:
    #             org.append((ascii_lowercase.find(c), True))
    #         else:
    #             org.append((ascii_uppercase.find(c), False))
    #     else:
    #         org.append(c)
    # for v in org:
    #     if type(v) is tuple:
    #         if v[1]:
    #             res.append(ascii_lowercase[(v[0] + key) % 26])
    #         else:
    #             res.append(ascii_uppercase[(v[0] + key) % 26])
    #     else:
    #         res.append(v)
    # return "".join(res)
