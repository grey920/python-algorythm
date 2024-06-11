"""
[중량제한]
https://www.acmicpc.net/problem/1939
- 이분 탐색을 통해 나를 수 있는 무게와 나를 수 없는 무게의 범위 나눔
-> 이분 탐색으로 나를 수 있는 최대 무게 찾을 수 있음
- 최대 중량을 매개 변수로 하여 이분 탐색 진행, 각 최대 중량마다 그래프 탐색을 해 출발 지점에서 도착 지점까지 이동할 수 있는지 판별하고,
 결과에 따라 이분 탐색의 탐색 범위를 갱신한다
"""
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
# 가중치(중량제한) 있는 무방향 그래프 생성
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, d = map(int, input().split())
    graph[x].append((y, d))
    graph[y].append((x, d))

# 이분탐색
start, end = map(int, input().split()) # 공장이 있는 두 섬
ans = 0 # 한 번의 이동에서 옮길 수 있는 물품들의 중량 최대값
left = 1
right = 10 ** 9 # 문제에서 주어진 중량의 최댓값
while left <= right:
    mid = (left + right) // 2 # 중간값. 이 값보다 큰 중량 제한을 가진 다리만 건널 수 있음
    visited = [False] * ( n + 1) # 그래프 탐색 초기 설정
    visited[start] = True
    q = [start]
    # BFS로 구현 (DFS도 됨)
    for idx in q:
        for adj, d in graph[idx]:
            if not visited[adj] and d >= mid: # 중량 제한을 넘어가는 다리는 건너지 않음
                visited[adj] = True
                q.append(adj)
    if visited[end]: # 목적지에 도착했다면 정답 갱신
        ans = mid
        left = mid + 1
    else:
        right = mid - 1
print(ans)


