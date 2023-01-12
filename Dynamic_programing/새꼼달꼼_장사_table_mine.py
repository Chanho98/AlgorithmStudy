def max_profit(price_list, count):
    # 최대이윤을 담아줄 사전을 만든다.
    profit_dic = {}

    # 0개 1개를 판매하는 경우를 미리 사전에 넣어 줍니다.
    profit_dic[0], profit_dic[1] = price_list[0], price_list[1]

    # 사전에 있는 경우
    if count in profit_dic:
        return profit_dic[count]

    # 사전에 없는 경우
    if count < len(price_list):
        profit = price_list[count]
    else:
        profit = 0

    for i in range(1, count // 2 + 1):
        profit = max(profit, max_profit(price_list, count - i)
                     + max_profit(price_list, i))

    profit_dic[count] = profit

    return profit_dic[count]


# 테스트
print(max_profit([0, 200, 600, 900, 1200, 2000], 5))
print(max_profit([0, 300, 600, 700, 1100, 1400], 8))
print(max_profit([0, 100, 200, 400, 600, 900, 1200, 1300, 1500, 1800], 9))

