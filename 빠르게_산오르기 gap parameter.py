def gap_in_stops(some_list):
    # 간격을 담아줄 리스트 생성
    gap_list = []

    for i in range(len(some_list) - 1):
        gap = some_list[i + 1] - some_list[i]
        gap_list.append(gap)

    return some_list[:1] + gap_list





def select_stops(water_stops, capacity):
    # 변수 설정
    current_height = 0
    stoped_location = []


    if min(gap_in_stops(water_stops)) > capacity:
        return "너무 높아 오를 수 없습니다."

    while current_height < water_stops[-1]:
        # 현재 물으로 올라갈 수 있는 최대 높이
        current_height += capacity

        if current_height > water_stops[-1]:
            # 정상에 도달 가능할 때
            current_height = water_stops[-1]

        for stop in range(len(water_stops)):
            if current_height - water_stops[stop] < 0:
                # 도달하지 못해다면 바로 이전이 최대 지점이다.
                current_height = water_stops[stop - 1]
                stoped_location.append(water_stops[stop - 1])
                break
            elif current_height - water_stops[stop] == 0:
                # 만약 물을 다 소진 했다면 그 지점이 최대 지점이다.
                current_height = water_stops[stop]
                stoped_location.append(water_stops[stop])
                break


    return stoped_location


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))

list3 = [1, 22, 24, 26]
print(select_stops(list3, 4))