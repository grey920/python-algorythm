"""템플릿으로 외우기"""
from heapq import *


def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heappop(pq) # 우선순위가 가장 높은 노드 추출
        if cur_v not in costs: # 방문 기록 확인
            costs[cur_v] = cur_cost # 현재 비용 업데이트
            for cost, next_v in graph[cur_v]: # 현재 노드의 인접 노드 확인
                next_cost = cur_cost + cost # 비용 계산
                heappush(pq, (next_cost, next_v)) # 계산한 비용을 우선순위 큐에 넣기
    return costs[final]


graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}
print(dijkstra(graph, 1, 8))
