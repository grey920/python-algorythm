"""
부녀회장이 될테야
https://www.acmicpc.net/problem/2775
"""


def number_of_residents(floor, room):
    memo = [[0] * (room + 1) for i in range(floor+1)]
    for i in range(room + 1):  # 0층 초기화
        memo[0][i] = i
    for i in range(floor+1):  # 각 층의 1호 초기화
        memo[i][1] = 1

    def dp_solution():
        for i in range(1, floor+1):  # 1층부터 ~
            for j in range(2, room + 1):  # 2호부터 ~
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]  # 이전 층 같은 호수 + 같은 층 이전 호수
        return memo[floor][room]

    return dp_solution()


def solution():
    t = int(input())
    for _ in range(t):
        k = int(input())
        n = int(input())
        print(number_of_residents(k, n))


solution()
