def selection_sort(unsorted_list):
    """선택 정렬 함수"""
    for i in range(len(unsorted_list)):
        min = unsorted_list[i]
        min_index = i
        for j in range(i + 1, len(unsorted_list)):
            if min > unsorted_list[j]:
                min = unsorted_list[j]
                min_index = j
        unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], unsorted_list[i]


    return unsorted_list





print(selection_sort([1, 4, 7, 2, 25, 87, 2, 4]))
print(selection_sort([9, 6, 23, 1, 143, 46, 241, 564, 675, 2, 342, 123124, 324]))

