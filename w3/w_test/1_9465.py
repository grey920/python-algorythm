"""
https://www.acmicpc.net/problem/9465
[접근방법]

"""
import sys

input = sys.stdin.readline


def max_sticker_point():
    col = int(input().strip())
    stamps = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * col for _ in range(2)]

    # 스티커 길이가 1인 경우
    dp[0][0] = stamps[0][0]
    dp[1][0] = stamps[1][0]
    if col == 1:
        return max(dp[0][0], dp[1][0])

    # 스티커 길이가 2인 경우 -> 대각선
    dp[0][1] = stamps[1][0] + stamps[0][1]
    dp[1][1] = stamps[0][0] + stamps[1][1]
    if col == 2:
        return max(dp[0][1], dp[1][1])

    # 스티커 길이가 3 이상일 경우 -> 대각선 or 하나 건너 대각선
    for i in range(2, col):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + stamps[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + stamps[1][i]

    return max(dp[0][-1], dp[1][-1])


def solution():
    t = int(input())
    for _ in range(t):
        print(max_sticker_point())


solution()
