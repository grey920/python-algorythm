# dfs
def dfs(cur_v):
    visited_dfs[cur_v] = True
    print(f'dfs={cur_v}', end=", ")

    for v in graph[cur_v]:
        if not visited_dfs[v]:
            dfs(v)


# bfs
from collections import deque


def bfs(start):
    visited_bfs = [False] * (node + 1)
    visited_bfs[start] = True

    queue = deque([start])
    while queue:
        cur_v = queue.popleft()
        print(cur_v, end=" ")
        for v in graph[cur_v]:
            if not visited_bfs[v]:
                visited_bfs[v] = True
                queue.append(v)


# 그래프 그리기
node = 5
graph = [[] for _ in range(node + 1)]
graph[5].append(4)
graph[4].append(5)

graph[5].append(2)
graph[2].append(5)

graph[1].append(2)
graph[2].append(1)

graph[3].append(4)
graph[4].append(3)

graph[3].append(1)
graph[1].append(3)

print(f'graph = {graph}')

# dfs
visited_dfs = [False] * (node + 1)
dfs(1)

# bfs
# bfs(3)
