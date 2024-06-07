"""
https://www.acmicpc.net/problem/1920
- N개 정수들 안에 M개 정수가 있는지 확인 -> 있으면 1, 없으면 0
"""


def search(sources, target):
    left = 0
    right = len(sources) - 1
    while left <= right:
        mid = (left + right) // 2
        if sources[mid] == target:
            return True
        elif sources[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


# 이분탐색, dictionary로 풀이 가능
n = int(input())
source_list = list(map(int, input().split()))
source_list.sort()  # 이분탐색을 위한 정렬

m = int(input())
target_list = list(map(int, input().split()))
for target in target_list:
    print(1 if search(source_list, target) else 0)
