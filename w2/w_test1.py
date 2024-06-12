"""
https://www.acmicpc.net/problem/1697
수빈이(N) -> 동생(K) 찾는 최단거리 시간 찾기
- 근데 그래프를 어떻게 그려야 하지? 4방향 찾는 것처럼 계산해야하나
"""
from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001


def bfs(start):
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


# result = bfs(n)
# print(result)

# 이 행동을 취하는게 무조건 이득인 상황에서 행동을 취하는 풀이
def find(n, k):
    if n >= k:  # n이 k보다 크거나 같으면 뺄셈으로 처리
        return n - k
    elif k == 1:  # k가 1 이면서, n이 k보다 작으면 -> n은 0
        return 1  # 따라서 1을 한 번 더해준다.
    elif k % 2:  # k 가 홀수이면 -> + 1 또는 - 1
        return min(find(n, k + 1), find(n, k - 1)) + 1
    else:  # k가 짝수이면 -> 2로 나눌 수 있음
        return min(k - n, find(n, k // 2) + 1)


print(find(n, k))
