# 제곱근 사용을 위한 sqrt 함수 - Brute Force
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

# 가장 가까운 두 매장을 찾아주는 함수
def closest_pair(coordinates):
    """언제나 첫 시행은 최소이자 최대가 된다."""
    pair = [coordinates[0], coordinates[1]]

    for fore in range(len(coordinates) - 1):
        for back in range(fore + 1, len(coordinates)):
            if distance(pair[0], pair[1]) > distance(coordinates[fore], coordinates[back]):
                pair[0], pair[1] = coordinates[fore], coordinates[back]

    return pair


# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest_pair(test_coordinates))


