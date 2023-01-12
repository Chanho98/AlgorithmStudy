def staircase_memo(n: int, cache: dict) -> int:

    # base case
    if n < 2:
        cache[n] = 1

    # 사전에 값이 있는 경우
    if n in cache:
        return cache[n]

    # 사전에 값이 없는 경우 계산후 저장해준다.
    cache[n] = staircase_memo(n - 1, cache) + staircase_memo(n - 2, cache)

    return cache[n]

def staircase(n):
    """Dynanic_programming_in_memoization"""
    stair_cache = {}

    return staircase_memo(n, stair_cache)

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))


