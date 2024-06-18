"""
쉽게 푸는 문제
https://www.acmicpc.net/problem/1292
"""


def make_arr_to_end(end):
    arr = []
    for i in range(1, end + 1):
        arr.extend([i] * i)

        if len(arr) > end:  # 끝나는 범위의 정수까지만 반복하도록 break
            break
    return arr


def solution():
    start, end = map(int, input().split())
    arr = make_arr_to_end(end)
    return sum(arr[start - 1:end])


print(solution())
