def max_product(left_cards, right_cards):
    """Brute Force / 무차별 대입기법 이용"""
    sum_list = []
    for left in range(len(left_cards)):
        for right in range(len(right_cards)):
            sum_list.append(left_cards[left] * right_cards[right])
    return max(sum_list)


# 테스트
print(max_product([1, 6, 5], [4, 2, 3]))
print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(max_product([-1, -7, 3], [-4, 3, 6]))