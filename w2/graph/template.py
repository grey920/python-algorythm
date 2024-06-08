graph = {}

# bfs
from collections import deque


def bfs(start_v):
    visited = [start_v]  # 첫 노드 방문
    queue = deque(start_v)

    while queue:
        cur_v = queue.popleft()  # dequeue
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited


bfs('A')

# dfs
visited_dfs = []


def dfs(cur_v):
    visited_dfs.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited_dfs:
            dfs(v)


dfs('A')
