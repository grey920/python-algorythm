"""
https://www.acmicpc.net/problem/1260
DFS와 BFS
"""

# 재귀 이용해 dfs 구현
from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

# 그래프 그리기
n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())  # 연결된 노드들
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in graph:
    i.sort()
print(graph)

# dfs
visited = [False] * (n + 1) # 그래프와 똑같은 모양으로 방문 여부 초기화
dfs(k)
print()

# bfs
visited = [False] * (n + 1)
bfs(k)
