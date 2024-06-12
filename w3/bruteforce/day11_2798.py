"""
https://www.acmicpc.net/problem/2798
[입력값]
5 21
5 6 7 8 9

[출력값]
21
"""
from itertools import combinations

n, m = map(int, input().split()) # 카드개수, 타겟

# 내림차순 정렬
cards = list(map(int, input().split()))

max_sum = 0
for card_combination in combinations(cards, 3):
    current_sum = sum(card_combination)
    if max_sum < current_sum <= m:
        max_sum = current_sum
print(max_sum)

# combi_list = combinations(cards, 3)
# sum_list = []
# for i in combi_list:
#     sum_list.append(sum(i))
#
# sum_list.sort()
# num = 0
# for i in sum_list:
#     if i <= m:
#        num = max(num, i)
#
# print(num)
