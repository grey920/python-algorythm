"""
https://www.acmicpc.net/problem/13975
가장 작은 파일 2개를 골라 하나가 될 떄까지 합친다
-> 계속 최소를 구하려면 우선순위큐? -> 힙?!
"""
import sys
import heapq

inputs = sys.stdin.readline


def convert_to_one_file():
    total_cost = 0
    chapter_cnt = int(inputs().strip())
    chapters = list(map(int, inputs().split()))
    heapq.heapify(chapters)

    # 최소 두개를 꺼냄 -> 두 수를 합치고 다시 힙에 넣기 -> 챕터수 -1
    while chapter_cnt > 1:
        min_1 = heapq.heappop(chapters)
        min_2 = heapq.heappop(chapters)

        cost = min_1 + min_2
        heapq.heappush(chapters, cost)

        chapter_cnt -= 1
        total_cost += cost

    return total_cost


t = int(inputs().strip()) # test case

for _ in range(t):
    print(convert_to_one_file())