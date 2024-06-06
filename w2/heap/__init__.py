"""
"""
import heapq

# 최소 힙 생성 및 삽입 ->
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)

# 최소값 확인 (최소 힙에서는 루트가 최소값)
# min_value = min_heap[0]
min_value = heapq.heappop(min_heap)
# print(f'최소값: {min_value}')
# print(f'최소힙: {min_heap}')

# 최대 힙 생성(음수 값 사용)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)

# 최대값 확인 (최대 힙에서는 루트의 음수값이 최대값)
max_value = -max_heap[0]
# print(f'최대 힙: {max_heap}')
# print(f'최대값: {max_value}')


###############################
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [(-1 * i, i) for i in max_heap] # [(-5, 5), (-3, 3), (-9, 9), (-4, 4), (-1, 1), (-2, 2), (-6, 6)]
heapq.heapify(max_heap) # [(-9, 9), (-4, 4), (-6, 6), (-3, 3), (-1, 1), (-2, 2), (-5, 5)]
weight, value = heapq.heappop(max_heap) # 튜플의 앞의 값을 기준으로 대소비교
print(value) # 9



