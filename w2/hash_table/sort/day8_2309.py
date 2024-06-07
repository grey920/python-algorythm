"""
https://www.acmicpc.net/problem/2309
- 리스트 정렬 -> O(nlogn)
- 투 포인터 탐색 -> O(n) (한 번의 선형 탐색)
=> O(nlogn)
"""


def solution(heights:list):
    heights_sum = sum(heights)
    target_sum = heights_sum - 100  # 7난장이가 아닌 난장이 두 명의 키 합

    heights.sort()  # 오름차순 정렬
    # 범인 난장이 두 명 찾기 (two pointer)
    left = 0
    right = len(heights) - 1
    while left <= right:
        if heights[left] + heights[right] == target_sum:
            return heights[left], heights[right]
        elif heights[left] + heights[right] > target_sum:
            right -= 1
        else:
            left += 1
    return None


heights = [int(input()) for _ in range(9)]
target_a, target_b = solution(heights)
heights.remove(target_a)
heights.remove(target_b)

for x in heights:
    print(x)
