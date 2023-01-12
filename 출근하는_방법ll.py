# 높이 n개의 계단을 올라가는 방법을 리턴한다
def stairs_memo(stairs, possible_steps, cache):
    # base case
    if stairs < 2:
        cache[stairs] = 1
        return cache[stairs]

    # 사전에 해당 값이 있는 경우
    if stairs in cache:
        return cache[stairs]

    # 사전에 해당 값이 없다면 추가후 등록해줍니다.
    # 우선 0으로 설정한 뒤 값을 추가해줍니다.
    # stairs보다 작은 possible_steps값들을 possible_Case에다 넣어줍니다
    cache[stairs] = 0
    possible_case = []

    for step in range(len(possible_steps)):
        if possible_steps[step] <= stairs:
            possible_case.append(possible_steps[step])

    # 경우의 수를 모두 더해준뒤 사전에 넣어준다.
    for n in possible_case:
        cache[stairs] += stairs_memo(stairs - n, possible_steps, cache)

    return cache[stairs]



def staircase(stairs, possible_steps):
    stair_cache = {}

    return stairs_memo(stairs, possible_steps, stair_cache)


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))