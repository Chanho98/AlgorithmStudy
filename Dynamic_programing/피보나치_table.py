def fib_tab(n):
    # 코드를 작성하세요.
    fib_dic = {
        1: 1,
        2: 1
    }

    # 기본으로 제공하는 dictionary에 있는 경우
    if n < 3:
        return fib_dic[n]

    # 사전에 없는 경우
    for add in range(3, n + 1):
        fib_dic[add] = fib_dic[add - 1] + fib_dic[add - 2]

    return fib_dic[n]



# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))

