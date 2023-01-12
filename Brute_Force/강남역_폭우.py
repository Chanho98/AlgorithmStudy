def trapping_rain(buildings):
    """layer 별로 계산 후 합산"""
    max_height = max(buildings)   # 최대 층수 구하기
    current_layer = 1             # 현재 계산 중인 층수
    trapped_rain = 0              # 물 저수량

    while current_layer <= max_height:
        buildings_position = []
        for i in range(len(buildings)):
            """빌딩이 있는 위치 리스트를 만들어 준다."""
            if buildings[i] >= current_layer:
                buildings_position.append(i)
        if len(buildings_position) > 1:
            """각 층마다 고여 있는 물량을 계산해 준다."""
            for j in range(len(buildings_position) - 1):
                trapped_rain += buildings_position[j + 1] - buildings_position[j] - 1
        current_layer += 1

    return trapped_rain

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))



def trapping_rain(buildings):
    # 총 담기는 빗물의 양을 변수에 저장
    total_height = 0

    # 리스트의 각 인덱스을 돌면서 해당 칸에 담기는 빗물의 양을 구한다
    # 0번 인덱스와 마지막 인덱스는 볼 필요 없다
    for i in range(1, len(buildings) - 1):
        # 현재 인덱스를 기준으로 양쪽에 가장 높은 건물의 위치를 구한다
        max_left = max(buildings[:i])
        max_right = max(buildings[i:])

        # 현재 인덱스에 빗물이 담길 수 있는 높이
        upper_bound = min(max_left, max_right)

        # 현재 인덱스에 담기는 빗물의 양을 계산
        # 만약 upper_bound가 현재 인덱스 건물보다 높지 않다면, 현재 인덱스에 담기는 빗물은 0
        total_height += max(0, upper_bound - buildings[i])

    return total_height

# 테스트
print(trapping_rain([0, 3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))