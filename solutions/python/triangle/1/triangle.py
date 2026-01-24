def equilateral(sides: list[int]):
    if not triangle_validate(sides):
        return False
    return sides[0] == sides[1] and \
        sides[0] == sides[2]


def isosceles(sides: list[int]):
    if not triangle_validate(sides):
        return False
    return sides[0] == sides[1] or \
        sides[0] == sides[2] or \
        sides[1] == sides[2]


def scalene(sides: list[int]):
    if not triangle_validate(sides):
        return False
    if isosceles(sides):
        return False
    return True


def triangle_validate(sides: list[int]):
    if any(x <= 0 for x in sides):
        return False
    if sum(sorted(sides)[:2]) < max(sides):
        return False
    return True
