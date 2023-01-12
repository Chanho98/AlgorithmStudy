def min_coin_count(value, coin_list):
    min_coin_counts = 0

    # coin_list를 내림차순으로 정렬해준다.
    coin_list.sort(reverse=True)

    # 크기가 큰 동전 순서로 연산해준다.
    for coin in coin_list:
        if value // coin != 0:
            coin_counts = value // coin
            value -= coin * coin_counts
            min_coin_counts += coin_counts


    return min_coin_counts

# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))



