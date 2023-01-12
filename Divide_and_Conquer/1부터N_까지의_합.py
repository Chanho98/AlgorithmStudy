# 핵심은 나누고<보통 양쪽 반으로 나눈다.>, 재귀적으로 구하고, 합하는 것이다.

def consecutive_sum(start, end):
    """base case & recursion case"""
    if start == end:
        return start
    else:
        return consecutive_sum(start, (start + end) // 2) + consecutive_sum((start + end) // 2 + 1, end)


# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))