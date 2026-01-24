"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list, list_two: list):
    if list_one == list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    str_one = " ".join(map(str, list_one))
    str_two = " ".join(map(str, list_two))
    if str_one in str_two and set(list_one).issubset(set(list_two)):
        return SUBLIST
    if str_two in str_one and set(list_two).issubset(set(list_one)):
        return SUPERLIST
    return UNEQUAL
