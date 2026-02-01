def total(basket: list[int]) -> int:
    prices = {
        1: 800,
        2: 1520,
        3: 2160,
        4: 2560,
        5: 3000,
    }

    count = [basket.count(i) for i in range(6)]
    dp = [[[[[0 for _ in range(count[5] + 1)]
             for _ in range(count[4] + 1)]
            for _ in range(count[3] + 1)]
           for _ in range(count[2] + 1)]
          for _ in range(count[1] + 1)]

    for a in range(count[1] + 1):
        for b in range(count[2] + 1):
            for c in range(count[3] + 1):
                for d in range(count[4] + 1):
                    for e in range(count[5] + 1):
                        min_price = float('inf')

                        # mask from 00001 to 11111
                        for mask in range(1, 32):
                            # size mean how much book bought
                            size = (mask & 1) + ((mask >> 1) & 1) + \
                                   ((mask >> 2) & 1) + ((mask >> 3) & 1) + \
                                   ((mask >> 4) & 1)

                            if size == 0 or size not in prices:
                                continue

                            na, nb, nc, nd, ne = a, b, c, d, e
                            valid = True

                            # check whether vaild to buy
                            if (mask & 1) and na > 0:
                                na -= 1
                            elif mask & 1:
                                valid = False

                            if valid and (mask >> 1) & 1:
                                if nb > 0:
                                    nb -= 1
                                else:
                                    valid = False

                            if valid and (mask >> 2) & 1:
                                if nc > 0:
                                    nc -= 1
                                else:
                                    valid = False

                            if valid and (mask >> 3) & 1:
                                if nd > 0:
                                    nd -= 1
                                else:
                                    valid = False

                            if valid and (mask >> 4) & 1:
                                if ne > 0:
                                    ne -= 1
                                else:
                                    valid = False

                            if not valid:
                                continue

                            # the mask group took how much
                            candidate = dp[na][nb][nc][nd][ne] + prices[size]
                            if candidate < min_price:
                                min_price = candidate

                        # if basket is []
                        if min_price == float('inf'):
                            min_price = 0

                        dp[a][b][c][d][e] = min_price

    return dp[count[1]][count[2]][count[3]][count[4]][count[5]]
