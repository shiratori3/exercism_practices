def spiral_matrix(size: int) -> list[int]:
    # init
    x, y = 0, 0
    min_x, min_y, max_x, max_y = 0, 0, size-1, size-1
    direction = "right"
    res = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size ** 2):
        # change direction and limit
        if x == max_x and y == min_y:
            min_y += 1 if direction != "down" else 0
            direction = "down"
        if x == max_x and y == max_y:
            max_x -= 1 if direction != "left" else 0
            direction = "left"
        if x == min_x and y == max_y:
            max_y -= 1 if direction != "up" else 0
            direction = "up"
        if x == min_x and y == min_y:
            min_x += 1 if direction != "right" else 0
            direction = "right"
        # fill num and move
        res[y][x] = i + 1
        if direction == "right":
            x += 1
        elif direction == "left":
            x -= 1
        elif direction == "up":
            y -= 1
        elif direction == "down":
            y += 1

    return res
