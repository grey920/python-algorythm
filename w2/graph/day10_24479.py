"""
[알고리즘 수업 - 깊이 우선 탐색 1]
https://www.acmicpc.net/problem/24479
- 시작 정점에서 방문할 수 없는 경우 0 출력
- 방문 순서 출력
- 인접 정점은 오름차순으로 방문
"""
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(cur_v):
    global count
    visited[cur_v] = count

    for next_v in graph[cur_v]:
        if visited[next_v] == 0:
            count += 1
            dfs(next_v)


node, edge, start = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(node + 1)]
for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(node+1):
    graph[i].sort()


# print(graph)
visited = [0] * (node + 1)
count = 1

dfs(start)

for i in range(1, node+1):
    print(visited[i])

