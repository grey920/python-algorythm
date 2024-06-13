"""
[청정수열]
https://www.acmicpc.net/problem/25176
[입력]
정수 N (1~10)
[출력]
점수가 최소인 청정수열의 개수
[문제 접근]
- 점수가 최소가 되는 청정수열을 만든다.
- 같은 정수끼리 있을때 사이에 더할 값이 없어서 가장 점수가 적다.
- => 1부터 N까지의 정수로 만들 수 있는 모든 수열의 개수 구하기
"""
from itertools import permutations
n = int(input())

arr = [x for x in range(1, n + 1)]
perm_list = list(permutations(arr, n))
print(len(perm_list))
