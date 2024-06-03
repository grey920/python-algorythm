"""
https://www.acmicpc.net/problem/2566
[전근 방법]
# 입력받은 문자열을 2차원 배열로 만들기
# 2차원 배열을 하나씩 판단하며 최대값과 해당 행, 열 정보를 저장한다
# 모든 순회가 끝나면 리턴
"""


# 입력받은 문자열을 2차원 배열로 만들기
def read_matrix(rows):
    return [list(map(int, input().split())) for _ in range(rows)]


# 2차원 배열을 하나씩 판단하며 최대값과 해당 행, 열 정보를 저장한다
def find_matrix(matrix):
    max_value = float('-inf')
    max_position = (0, 0)
    for i in range(9):
        for j in range(9):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
    # 모든 순회가 끝나면 리턴
    return max_value, max_position[0] + 1, max_position[1] + 1


# 1. 입력 받은 문자열 행렬을 읽어 리스트로 반환
matrix = read_matrix(9)

# 2. 최댓값과 i, j 값 리턴받음
max_value, max_i, max_j = find_matrix(matrix)
print(max_value)
print(max_i, max_j)
