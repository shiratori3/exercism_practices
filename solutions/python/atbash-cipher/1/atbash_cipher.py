from string import ascii_lowercase, ascii_letters


def encode(plain_text: str) -> str:
    encoded = "".join(
        [ascii_lowercase[25 - ascii_lowercase.find(c.lower())]
        if c in ascii_letters
        else "" if c in ",.!"
        else c.strip() for c in plain_text]
    )
    return " ".join([encoded[i:i+5] for i in range(0, len(encoded), 5)])


def decode(ciphered_text: str) -> str:
    return "".join([ascii_lowercase[25 - ascii_lowercase.find(c)]
                    if c in ascii_lowercase
                    else c.strip() for c in ciphered_text])
