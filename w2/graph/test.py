# 1. 간선에 비중이 있다면 graph[x][y]에 비중을 넣는다
"""
n = 4 # 전체 노드의 갯수
graph = [[False] * n for _ in range(n)] # 그래프 초기 설정
graph[0][2] = True # 0번 노트에서 2번 노드로 가는 간선이 존재

print(graph)
"""

# 2. 비중이 있는 간선은 튜플을 이용해 (끝점, 비중) 으로 나타낼 수 있다
graph = [
    [1],
    [0, 2],
    [1, 3],
    [2]
]

graph[1].append(3)
print(graph)