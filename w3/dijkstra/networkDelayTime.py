"""개발남노씨"""
import heapq
from collections import defaultdict


def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1])) # time[0]: 노드, 1: 인접노드, 2: 가중치

    costs = {} # 방문기록
    pq = [] # 우선순위 큐
    heapq.heappush(pq, (0, k)) # 시작노드는 비용 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))

    for node in range(1, n+1):
        if node not in costs:
            return -1
    return max(costs.values())



result = network_delay_time(times=[[2, 1, 2], [2, 3, 5], [2, 4, 1], [4, 3, 3]], n=4, k=2)
print(result)
