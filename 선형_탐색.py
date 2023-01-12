def linear_search(element, some_list):
    """리스트 선형 탐색 함수"""
    for index in range(len(some_list)):
        # 만일 찾는 값이 있으면, 인덱스값을 return 해준다.
        if element == some_list[index]:
            return index

    return None  # 만일 찾는 값이 없다면, None을 리턴해준다.



# 테스트 코드
print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))