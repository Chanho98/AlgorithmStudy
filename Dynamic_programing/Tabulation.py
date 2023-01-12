# proto_type
def fib_tab(n):
    fib_table = [1]

    previous = 0
    current = 1
    bottom_up_num = 0

    while bottom_up_num < n:
        previous, current = current, previous + current
        fib_table.append(current)

        bottom_up_num += 1

    return fib_table[n - 2] + fib_table[n - 3]


# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))


# fib_optimize

def fib(n):
    # 상수 설정
    previous = 0
    current = 1

    for i in range(1, n):
        """tip i 변수를 사용하지 않더라도 반복문 사용 가능"""
        previous, current = current, previous + current

    return current

print(fib(6))
print(fib(50))
print(fib(21))


# 미리 계산된 값을 몇개 넣어주면 편하다.
def fib_tab(n):
    # 이미 계산된 피보나치 수를 담는 리스트
    fib_table = [0, 1, 1]

    # n번째 피보나치 수까지 리스트를 하나씩 채워 나간다
    for i in range(3, n + 1):
        fib_table.append(fib_table[i - 1] + fib_table[i - 2])

    # 피보나치 n번째 수를 리턴한다
    return fib_table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))



