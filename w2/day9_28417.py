"""
https://www.acmicpc.net/problem/28417
- n만큼 순회하면서
-> 1명의 런 점수 / 트릭점수 각각 정렬
-> 런 맥스 + 트릭 높은 2개 => 최종 최고점수
=> n명중 가장 높은 점수를 리턴
"""
import sys

input = sys.stdin.readline
n = int(input().strip())
points_list = []


def get_max_point(arr):
    arr = list(map(int, arr.split()))
    run, trick = arr[:2], arr[2:]
    run_point = max(run)
    trick_point = sum(sorted(trick, reverse=True)[:2])
    return run_point + trick_point


for _ in range(n):
    max_point = get_max_point(input().strip())
    points_list.append(max_point)

print(max(points_list))
