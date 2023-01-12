def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 주어지지 않은 경우
    if end_index == None:
        end_index = len(some_list) - 1

    """base case1 - 해당 리스트에 element가 없는 경우"""
    if start_index > end_index:
        return None

    mid_index = (start_index + end_index) // 2
    """base case2"""
    if some_list[mid_index] == element:
        return mid_index

    """recursion case"""
    if some_list[mid_index] > element:
        return binary_search(element, some_list, start_index, mid_index - 1)
    if some_list[mid_index] < element:
        return binary_search(element, some_list, mid_index + 1, end_index)

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))