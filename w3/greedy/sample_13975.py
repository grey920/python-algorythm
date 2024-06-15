"""
파일합치기 3
https://www.acmicpc.net/problem/13975
"""
from sys import stdin
from heapq import *

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    ans = 0

    for _ in range(n-1): # 가장 작은 크기의 두 파일을 합치는 게 제일 이득!
        a = heappop(files)
        b = heappop(files)
        ans += a + b
        heappush(files, a + b)
    print(ans)