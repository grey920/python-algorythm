"""
[최소 힙] https://www.acmicpc.net/problem/1927
- 입력에서 0이 주어진 횟수만큼 답 출력
- 배열이 비어있으면 0 출력
"""
import heapq
from sys import stdin
inputs = stdin.readline

N = int(inputs()) # 연산의 개수

heap = [] # 비어있는 배열에서 시작
# 연산정보 x ( 0이면 가장 작은 값 출력 및 제거 ->heap pop / 자연수면 x를 추가 heap push)
for _ in range(N):
    # print(int(inputs()))
    x = int(inputs())

    if x > 0: # 자연수면 heap push
        heapq.heappush(heap, x)
    else: # 0 일때
        if not heap: # 배열이 비어있으면 0
            print(0)
        else: # 배열에 요소가 있으면 pop
            print(heapq.heappop(heap))



