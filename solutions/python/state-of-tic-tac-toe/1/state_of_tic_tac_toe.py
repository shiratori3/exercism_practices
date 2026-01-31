from itertools import product


def gamestate(board: list[str]) -> str:
    board_filled = False
    cnt_X, cnt_O = 0, 0
    for _ in board:
        cnt_X += sum(1 if c == "X" else 0 for c in _)
        cnt_O += sum(1 if c == "O" else 0 for c in _)
    print(cnt_X, cnt_O)
    if cnt_X - cnt_O < 0:
        raise ValueError("Wrong turn order: O started")
    if cnt_X - cnt_O > 1:
        raise ValueError("Wrong turn order: X went twice")

    winner = dict.fromkeys(["X", "O"], 0)
    if cnt_X + cnt_O == 9:
        board_filled = True
    for x in range(3):
        for y in range(3):
            # skip 4 corner
            if (x, y) in list(product([0, 2], repeat=2)):
                continue
            # skip blank
            char = board[x][y]
            if char not in ["O", "X"]:
                continue
            # check same
            for dx, dy in [(-1, -1), (-1, 0), (0, -1), (1, -1)]:
                x1, y1 = x + dx, y + dy
                x2, y2 = x - dx, y - dy
                if 0 <= x1 <= 2 and 0 <= x2 <= 2 and 0 <= y1 <= 2 and 0 <= y2 <= 2:
                    if char == board[x1][y1] and char == board[x2][y2]:
                        winner[char] += 1

    if winner["X"] > 0 and winner["O"] > 0:
        raise ValueError("Impossible board: game should have ended after the game was won")
    elif winner["X"] > 0 or winner["O"] > 0:
        return "win"

    if board_filled:
        return "draw"
    else:
        return "ongoing"
