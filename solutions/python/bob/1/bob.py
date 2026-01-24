def response(hey_bob: str):
    if not hey_bob.strip():
        return "Fine. Be that way!"
    if hey_bob.isascii():
        if hey_bob.isupper():
            if hey_bob[-1] == "?":
                return "Calm down, I know what I'm doing!"
            return "Whoa, chill out!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    return "Whatever."
