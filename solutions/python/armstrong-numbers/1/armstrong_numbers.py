def is_armstrong_number(number):
    return number == sum([pow(int(char), len(str(number))) for char in list(str(number))])
