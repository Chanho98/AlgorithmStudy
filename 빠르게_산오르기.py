def select_stops(water_stops, capacity):
    # 변수 설정
    current_height = 0
    stoped_location = []


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

list3 = [1, 4, 5, 7, 11, 12, 13, 16, 22, 24, 26]
print(select_stops(list3, 4))



def select_stops(water_stops, capacity):
    # 약수터 위치 리스트
    stop_list = []

    # 마지막 들른 약수터 위치
    prev_stop = 0

    for i in range(len(water_stops)):
        # i 지점까지 갈 수 없으면, i - 1 지점 약수터를 들른다
        if water_stops[i] - prev_stop > capacity:
            stop_list.append(water_stops[i - 1])
            prev_stop = water_stops[i - 1]

    # 마지막 약수터는 무조건 간다
    stop_list.append(water_stops[-1])

    return stop_list


# 테스트
list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))