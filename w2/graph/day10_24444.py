"""
[알고리즘 수업 - 너비 우선 탐색 1]
https://www.acmicpc.net/problem/24444
"""
import sys
from collections import deque

inputs = sys.stdin.readline

count = 1


def bfs(start):
    global count
    visited[start] = count
    queue = deque([start]) # 앗.. deque(graph[start]) 로 초기화해서 계속 망했다..ㅎ

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if visited[v] == 0:
                # print(f'cur_v = {cur_v}, visited[v]={visited[v]}')
                count += 1
                visited[v] = count
                queue.append(v)


node, edge, start = map(int, inputs().split())

# 그래프
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    a, b = map(int, inputs().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, node + 1):
    graph[i].sort()
# print(graph)
visited = [0] * (node + 1)

bfs(start)

for i in range(1, node+1):
    print(visited[i])
