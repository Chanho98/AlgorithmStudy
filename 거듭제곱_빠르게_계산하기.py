def power(x, y):
    """base case"""
    if y == 0:
        return 1

    if y == 1:
        return x

    """recursion case"""
    # y = y - (y // 2) + (y // 2)에서 가져온 아이디어 입니다.
    return power(x, y // 2) * power(x, y - y // 2)

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))