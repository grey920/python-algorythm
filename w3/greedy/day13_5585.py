"""
거스름돈
https://www.acmicpc.net/problem/5585
[입력]
380
[출력]
4
[접근방법]

"""


def solution(pay):
    change = 1000 - pay
    coins = [500, 100, 50, 10, 5, 1]
    answer = 0

    for coin in coins:
        answer += change // coin
        change %= coin
    return answer


pay = int(input())
print(solution(pay))
