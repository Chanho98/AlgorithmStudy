def min_fee(pages_to_print):
    # 벌금을 담을 변수 생성
    penalty_sum = 0
    people_to_pay = len(pages_to_print)

    # 내림차순으로 정리하여 주는 것이 Point다
    pages_to_print.sort()

    # 프린트를 적은 수부터 뽑아주고 제거해준다.
    for page in pages_to_print:
        penalty_sum += page * people_to_pay
        people_to_pay -= 1


    return penalty_sum


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))
