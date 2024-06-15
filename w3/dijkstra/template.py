"""템플릿으로 외우기"""
from heapq import *


def dijkstra2(graph, start, end):
    distance = [float("inf")] * (end + 1)  # 최소 비용을 기록할 배열. 처음엔 무한대로 초기화
    distance[start] = 0  # 첫 노드는 자기 자신이므로 비용 0
    q = []  # 우선순위 큐
    heappush(q, (0, start))
    while q:
        cur_cost, cur_v = heappop(q)  # 큐에서 우선순위 가장 높은 노드 추출
        if distance[cur_v] < cur_cost:  # 큐에서 꺼낸 노드의 비용이 distance 배열에 적힌 비용보다 크면 갱신하지않고 넘어감
            continue
        for cost, next_v in graph[cur_v]:
            next_cost = distance[cur_v] + cost
            if next_cost < distance[next_v]:
                distance[next_v] = next_cost
                heappush(q, (next_cost, next_v))
    return distance[end]


def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_cost, cur_v = heappop(pq)  # 우선순위가 가장 높은 노드 추출
        if cur_v not in costs:  # 방문 기록 확인
            costs[cur_v] = cur_cost  # 현재 비용 업데이트
            for cost, next_v in graph[cur_v]:  # 현재 노드의 인접 노드 확인
                next_cost = cur_cost + cost  # 비용 계산
                heappush(pq, (next_cost, next_v))  # 계산한 비용을 우선순위 큐에 넣기
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
print(f'다익스트라 1 ::: {dijkstra(graph, 1, 8)}')
print(f'다익스트라 2 ::: {dijkstra2(graph, 1, 8)}')
