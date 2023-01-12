# AlgorithmStudy
파이썬 언어를 이용하여 여러 알고리즘을 구현

## 1. Brute Force
전체를 탐색해보는 알고리즘으로 반복문을 이용하여 모든 범위를 탐색하는 알고리즘이다.
알고리즘의 구현이 매우 쉽다는 장점이 존재하지만, 연산량이 많기 때문에 비효율적이라는 단점이 존재한다.
## 2.1 Divide and Conquer
주어진 문제를 더 이상 나눌 수 없을 때까지 나눈뒤에 풀며 다시 합치는 과정을 통해 문제의 답을 얻는 알고리즘이다.

## 2.2. 분활 정복 알고리즘을 통하여, 리스트 정렬 구현
```
def merge(list1, list2):
    i = 0
    j = 0

    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1과 list2를 돌면서 merged_list에 항목 정렬
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        else:
            merged_list.append(list1[i])
            i += 1

    # list2에 남은 항목이 있으면 정렬 리스트에 추가
    if i == len(list1):
        merged_list += list2[j:]

    # list1에 남은 항목이 있으면 정렬 리스트에 추가
    elif j == len(list2):
        merged_list += list1[i:]

    return merged_list


def merge_sort(my_list):
    # base case
    if len(my_list) < 2:
        return my_list

    # my_list를 반씩 나눈다(divide)
    left_half = my_list[:len(my_list)//2]    # 왼쪽 반
    right_half = my_list[len(my_list)//2:]   # 오른쪽 반

    # merge_sort 함수를 재귀적으로 호출하여 부분 문제 해결(conquer)하고,
    # merge 함수로 정렬된 두 리스트를 합쳐(combine)준다
    return merge(merge_sort(left_half), merge_sort(right_half))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
```
테스트 코드를 실행한 결과
```
[1, 3, 5, 7, 9, 11, 11, 13]
[1, 5, 7, 9, 13, 15, 28, 30, 48]
[1, 1, 2, 2, 4, 4, 4, 5, 6, 6, 7, 7, 10, 11, 13, 15]
```
리스트 요소들이 제대로 정렬됨을 확인 할 수 있다.
## 3.1. Dynamic Programing
큰 문제를 작은 문제로 나누어 푸는 방식으로 동적 프로그래밍이라고도 부른다. 분활정복 알고리즘과의 차이는 작게 분활한 문제들이 반복되는 것을 이용해서 풀어나가는 방식이라는 점이다. 이 때 작은 문제에서의 계산 값을 저장하여 두고 문제를 해결해 나가는데 이를 Memorization이라 한다.

## 3.2. 동적 프로그래밍을 이용한 피보나치 수열 구현
```
def fib_memo(n, cache):
    # base case
    if n < 3:
        return 1

    # 이미 n번째 피보나치를 계산했으면:
    # 저장된 값을 바로 리턴한다
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면:
    # 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)

    # 계산한 값을 리턴한다
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
```
테스트 코드 실행 결과
```
55
12586269025
354224848179261915075
```

## 4. Greedy Algorithm

## 5. Recursion Function
