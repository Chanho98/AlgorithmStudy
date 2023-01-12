# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list


# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = end
    big = start
    indicater = start

    while indicater < pivot:
        # pivot보다 indicater가 크거나 같은 경우
        if my_list[indicater] >= my_list[pivot]:
            indicater += 1
        # pivot보다 indicater가 작은 경우
        else:
            swap_elements(my_list, big, indicater)
            big += 1
            indicater += 1

    # 실행이 끝나고 indicater가 pivot에 도달 했을때,
    if indicater == pivot:
        swap_elements(my_list, big, pivot)
        pivot = big

    # pivot의 위치를 리턴해 준다.
    return pivot


# 퀵 정렬
def quicksort(my_list, start, end):
    # base case - merge메소드와 다르게 범위만 줄어들 뿐, 실제 리스트가 주는 것이 아니므로 범위로 설정한다.
    if end - start < 1:
        # 리턴은 한 줄 뿐만 아니라 아래와 같이 실행 할 수도 있다.
        return

    # my_list를 두 부분으로 나누어주고,
    # partition 이후 pivot의 인덱스를 리턴받는다
    pivot = partition(my_list, start, end)

    # pivot의 왼쪽 부분 정렬
    quicksort(my_list, start, pivot - 1)

    # pivot의 오른쪽 부분 정렬
    quicksort(my_list, pivot + 1, end)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)