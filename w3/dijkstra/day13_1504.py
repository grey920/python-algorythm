"""
특정한 최단 경로
https://www.acmicpc.net/problem/1504
[입력]
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
[출력]
7
[접근방법]
최단 경로 -> 다익스트라
한번 이동했어도 가능, 반드시 주어진 두 정점 거쳐야 한다..?

"""
from heapq import *
import sys
from collections import defaultdict

input = sys.stdin.readline


def dijkstra(start, final):
    costs = {}
    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_cost, cur_node = heappop(pq)

    return


def solution():
    answer = -1  # 경로가 없는 경우 -1을 초기값으로 설정
    graph = defaultdict(list)

    n, e = map(int, input().split())
    for _ in range(e):
        a, b, c = map(int, input().split())
        # 무방향 그래프
        graph[a].append((c, b))
        graph[b].append((c, a))

    v1, v2 = map(int, input().split())

    answer = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n),
                 dijkstra(1, v1) + dijkstra(v2, v1) + dijkstra(v1, n))
    return answer


print(solution())
