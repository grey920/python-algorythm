"""
https://www.acmicpc.net/problem/1697
수빈이(N) -> 동생(K) 찾는 최단거리 시간 찾기
- 근데 그래프를 어떻게 그려야 하지? 4방향 찾는 것처럼 계산해야하나
"""
from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001


def bfs(start):
    shortest_time = 0
    visited[start] = True
    queue = deque()
    queue.append((start, 0))

    while queue:
        cur_v, cur_len = queue.popleft()
        # 찾은 경우
        if cur_v == k:
            return cur_len

        for next_v in (cur_v - 1, cur_v + 1, cur_v * 2):
            if 0 <= next_v <= 100_000 and not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, cur_len + 1))


result = bfs(n)
print(result)
