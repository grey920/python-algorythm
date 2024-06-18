"""
적어도 대부분의 배수
https://www.acmicpc.net/problem/1145
[접근방법]
- 완전탐색 -> 세 정수를 조합하여 나오는 lcm을 모두 구한다 -> 최소값 구하기
"""
import math
import sys


def solution():
    arr = list(map(int, input().split()))
    min_lcm = sys.maxsize
    for i in range(len(arr)-2):
        for j in range(i + 1, len(arr)-1):
            for k in range(j+1, len(arr)):
                lcm = math.lcm(arr[i], arr[j], arr[k])
                min_lcm = min(min_lcm, lcm)

    return min_lcm


print(solution())
