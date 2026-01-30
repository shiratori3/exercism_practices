def find(search_list: list[int], value: int) -> int:
    if not search_list or value not in search_list:
        raise ValueError("value not in array")
    x, y = 0, len(search_list) - 1
    while True:
        mid = (x + y) // 2
        if value == search_list[mid]:
            return mid
        if x + 1 == y:
            return mid + 1
        if value < search_list[mid]:
            y = mid
        elif value > search_list[mid]:
            x = mid
