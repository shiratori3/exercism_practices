def convert(number: int) -> str:
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    return "".join(["Pling" if number % 3 == 0 else "",
                    "Plang" if number % 5 == 0 else "",
                    "Plong" if number % 7 == 0 else ""])
