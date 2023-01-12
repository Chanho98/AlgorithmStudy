# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    """base case"""
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    """recursion case"""
    if len(some_list) > 1:
        return  some_list[-1:] + flip(some_list[0 : len(some_list) - 1])



# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list):
    """base case"""
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list

    """recursion case""" - 이렇게 [-1]를 하면 리스트가 아니라 인덱스가 변환되어서 연산에 오류가 생긴다.
    if len(some_list) > 1:
        return  some_list[-1] + flip(some_list[0 : len(some_list) - 1])



# 테스트
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = flip(some_list)
print(some_list)

