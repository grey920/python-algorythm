"""
문어
https://www.acmicpc.net/problem/21313
"""

def solution():
    n = int(input())
    answer = []

    for i in range(n):
        if n % 2 != 0 and i == n - 1: # n이 홀수 -> 첫 항과 마지막 항 모두 1이 겹침 -> 마지막 항을 3으로 셋팅
            answer.append(3)
        elif i % 2 == 0:
            answer.append(1)
        else:
            answer.append(2)
    return ' '.join(map(str, answer))


print(solution())