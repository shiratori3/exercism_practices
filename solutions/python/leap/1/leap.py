def leap_year(year: int) -> bool:
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    return True
