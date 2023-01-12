def max_profit_memo(price_list, count, cache):
    """base case"""
    if count < 2:
        cache[count] = price_list[count]
        return cache[count]

    # 최대값을 담아줄 변수를 설정한다. profit
    # 한 사람에게 최대한 파는게 가능한 경우 최대한 파는 것으로 최대값을 설정한다.
    # 만일 한 사람에게 파는게 가능한 범위를 벗어난다면 0으로 설정한다.
    """recursion case"""
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit_memo(price_list, count - i, cache)
                     + max_profit_memo(price_list, i, cache))

    cache[count] = profit

    return profit


def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
