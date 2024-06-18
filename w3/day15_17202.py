"""
https://www.acmicpc.net/problem/17202

dp 테이블
[
    [10, 10, 8, 14, 14, 12, 10, 10],
    [0, 8, 2, 8, 6, 2, 0],
    [8, 0, 0, 4, 8, 2],
    [8, 0, 4, 2, 0],
    [8, 4, 6, 2],
    [2, 0, 8],
    [2, 8]
]
"""


def sum_ab(a, b):
    numbers = []
    for l, r in zip(a, b):
        numbers.append(int(l))
        numbers.append(int(r))
    return numbers


def dp_solution(a, b):
    initial = sum_ab(a, b)  # 초기 값을 계산하여 DP 테이블의 첫 번째 행에 저장
    dp = [initial]  # DP 테이블 초기화

    while len(dp[-1]) > 2:  # 숫자 문자열의 길이가 2가 될 때까지 반복
        current = dp[-1]  # 현재 단계의 결과
        next_stage = []

        # 인접한 숫자들의 합을 계산하여 새로운 단계의 결과를 만듦
        for i in range(len(current) - 1):
            next_value = (int(current[i]) + int(current[i + 1])) % 10
            next_stage.append(str(next_value))

        dp.append(next_stage)  # 새로운 단계의 결과를 DP 테이블에 추가

    # 최종 결과 반환
    return ''.join(dp[-1])


def solution():
    import sys
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()

    return dp_solution(a, b)


print(solution())