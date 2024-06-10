"""
[촌수계산]
https://www.acmicpc.net/problem/2644
=> 가중치가 있는 그래프 탐색. 못찾으면 -1
[입력]
1) 전체 사람 수 n
2) 서로 다른 두 사람의 번호
3) 부모-자식 관계 개수 m
4) 부모-자식 관계 번호 x(부모), y(자식)
[출력]
- 두 사람의 촌수. 친척 관계가 전혀 없으면 -1 출력
"""
import sys

inputs = sys.stdin.readline

n = int(inputs().strip()) # 전체 수
start, end = map(int, inputs().split()) # 촌수 찾을 두 사람

graph = [[] for _ in range(n+1)] # 0번 인덱스 버림

# 상하 간선 개수 (그래프 생성)
edge = int(inputs().strip())
for _ in range(edge):
    parent, child = map(int, inputs().split())
    graph[parent].append(child)
    graph[child].append(parent)

visited = [False for _ in range(n + 1)]


def dfs(cur_v, count):
    global flag # 마지막에 못찾을 경우를 위한 플래그
    visited[cur_v] = True
    if cur_v == end:
        flag = True
        print(count)
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v, count+1)


flag = False
dfs(start, 0)
if not flag:
    print(-1)

