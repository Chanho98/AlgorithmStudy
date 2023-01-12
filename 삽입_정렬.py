def insertion_sort(unsorted_list):
    for i in range(len(unsorted_list)):
        for j in range(i - 1, -1, -1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list


print(insertion_sort([1, 4, 7, 2, 25, 87, 2, 4]))
print(insertion_sort([9, 6, 23, 1, 143, 46, 241, 564, 675, 2, 342, 123124, 324]))

