"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id: list, missing_wagons: list):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    for index, value in enumerate(each_wagons_id[2:]):
        if value == 1:
            res = each_wagons_id[2:]
            res[index + 1:index + 1] = missing_wagons
            res.append(each_wagons_id[0])
            res.append(each_wagons_id[1])
            return res


def add_missing_stops(route: dict, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route.setdefault("stops", list(kwargs.values()))
    return route


def extend_route_information(route: dict, more_route_information: dict):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return route | more_route_information


def fix_wagon_depot(wagons_rows: list[list[tuple]]):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    combine_lists = [t for sublist in wagons_rows for t in sublist]
    return [combine_lists[i::3] for i in range(3)]
