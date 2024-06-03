"""
https://www.acmicpc.net/problem/2738
"""
N, M = map(int, input().split())

# N개의 행을 가진 행렬 a
a = [list(map(int, input().split())) for _ in range(N)]
# N개의 행을 가진 행렬 b
b = [list(map(int, input().split())) for _ in range(N)]

# 덧셈 연산 결과를 담을 2차원 배열
result = [[0] * M for _ in range(N)]

# 덧셈 연산
for i in range(N):
    for j in range(M):
        result[i][j] = a[i][j] + b[i][j]

# 결과 행렬을 문자열로 변환
for row in result:
    print(' '.join(map(str, row)))
