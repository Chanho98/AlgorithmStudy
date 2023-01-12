def max_profit(stock_list):
    """Brutal Forxe"""
    profit_list = []

    for i in range(len(stock_list) - 1):
        for j in range(i + 1, len(stock_list)):
            profit = stock_list[j] - stock_list[i]
            profit_list.append(profit)

    return max(profit_list)


# 테스트
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))



def max_profit(stock_list):
    """Greedy algorism"""

    profit_list = []

    for pivot in range(len(stock_list) - 1):
        """매매 일로부터 가장 고가일 때, 처분한다."""
        right_side = stock_list[pivot + 1:]
        profit_list.append(max(right_side) - stock_list[pivot])

    return max(profit_list)

print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([11, 13, 9, 13, 20, 14, 19, 12, 19, 13]))
print(max_profit([12, 4, 11, 18, 17, 19, 1, 19, 14, 13, 7, 15, 10, 1, 3, 6]))
