"""
카드놓기
https://www.acmicpc.net/problem/5568
[입력]
n: 전체 카드 개수
k: 선택할 카드 개수
다음줄부터~: n개의 카드 숫자
[출력]
만들 수 있는 정수 개수
[접근 방법]
- 순열을 만들고 set으로 중복을 없애보자
"""
import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input().strip())
k = int(input().strip())

cards = [input().strip() for _ in range(n)]
unique_numbers = set()

for perm in permutations(cards, k):
    number = ''.join(perm)
    unique_numbers.add(int(number))

print(len(unique_numbers))














# arr = []
# for _ in range(n):
#     arr.append(input().split())
# perm = list(permutations(arr, k))
#
# integer_arr = []
# for val in perm:
#     integers = ''
#     for i in range(k):
#         integers += val[i][0]
#     integer_arr.append(int(integers))
#
# print(len(set(integer_arr)))