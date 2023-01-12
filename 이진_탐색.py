def binary_search(element: str, some_list: list) -> int or None:
    start_index = 0
    end_index = len(some_list) - 1

    while start_index <= end_index:
        # start_index 가 end_index 보다 커진다면 실행 종료
        mid_index = (start_index + end_index) // 2

        # 만일 mid_index 가 element 라면 mid_index 를 리턴한다.
        if some_list[mid_index] == element:
            return mid_index
        # 만일 element 보다 작다면 start + 1을 해준다.
        elif some_list[mid_index] < element:
            start_index = mid_index + 1
        # 만일 element 보다 크다면 end - 1을 해준다.
        else:
            end_index = mid_index - 1

    return None   # 찾는 값이 없다면 None을 리턴한다.



# 테스트 코드
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))