"""
https://www.acmicpc.net/problem/2566
[전근 방법]
# 입력받은 문자열을 2차원 배열로 만들기
# 2차원 배열을 하나씩 판단하며 최대값과 해당 행, 열 정보를 저장한다
# 모든 순회가 끝나면 리턴
"""
# 입력받은 문자열을 2차원 배열로 만들기
a = []
for _ in range(9):
    a.append(list(map(int, input().split())))
# 2차원 배열을 하나씩 판단하며 최대값과 해당 행, 열 정보를 저장한다
max_value = 0
max_i = 0
max_j = 0
for i in range(9):
    for j in range(9):
        if a[i][j] > max_value:
            max_value = a[i][j]
            max_i = i
            max_j = j
# 모든 순회가 끝나면 리턴
print(max_value, max_i+1, max_j+1)