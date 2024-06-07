def insertion_sort(arr):
    for i in range(1, len(arr)):  # 1번 인덱스 ~ 끝
        key = arr[i]  # 정렬 대상 값
        j = i - 1  # 비교 대상 인덱스
        while j >= 0 and key < arr[j]:  # 정렬 대상 값 < 비교 대상 값
            arr[j + 1] = arr[j]
            j -= 1  # 비교 대상 자리를 앞으로 이동
        arr[j + 1] = key  # 삽입될 위치 찾으면 -> 비교 대상 인덱스 다음 위치에 정렬 대상 값 부여


def bubble_sort(arr):
    n = len(arr)  # 6
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # 인접한 두 수 비교
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # temp없이 교체가 되네..?
            print(f'교환후 = {arr}')


def quick_sort(arr):
    print(f'arr = {arr}')
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # 배열의 중앙 인덱스의 값이 기준
    # print(len(arr)//2, pivot)
    left = [x for x in arr if x < pivot]  # 피봇보다 작은 값들만 추림
    middle = [x for x in arr if x == pivot]  # 피봇과 동일한 값만 추림
    right = [x for x in arr if x > pivot]  # 피봇보다 큰 값들만 추림
    # 재귀적으로 호출
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """중앙 인덱스를 기준으로 재귀적으로 나눔"""
    if len(arr) <= 1:  # 재귀 호출의 base
        return arr
    mid = len(arr) // 2  # 배열의 중앙 인덱스
    left = merge_sort(arr[:mid])  # 배열 처음부터 중앙 -1까지 재귀 호출
    right = merge_sort(arr[mid:])  # 배열 중앙부터 끝까지 재귀 호출

    return merge(left, right)


def merge(left, right):
    """합치면서 정렬"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # 작은 수를 result에 담음
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


import heapq


def heap_sort(arr):
    heapq.heapify(arr)  # 배열을 힙으로 변환
    sorted_arr = []
    while arr:
        sorted_arr.append(heapq.heappop(arr))  # 힙에서 '최소값' 추출 -> 배열에 추가
    return sorted_arr


# 예제 데이터
data = [5, 2, 9, 1, 5, 6]

# insertion_sort(data) # 삽입 정렬
# bubble_sort(data) # 버블 정렬
# result = quick_sort(data)
# merge_sort(data)  # 병합 정렬
heap_sort(data)
