"""
https://www.acmicpc.net/problem/1927

"""
import heapq
import sys

input = sys.stdin.readline

# 연산의 개수
N = int(input())
# 힙 생성
heap = []

# 연산 정보 (0이면 최소값 출력, 자연수면 추가 연산)
for _ in range(N):
    a = int(input())
    if a:
        heapq.heappush(heap, a)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)

