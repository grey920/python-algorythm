"""
https://www.acmicpc.net/problem/10798
[문제분석]
- 행과 열을 바꾸기
"""
list_2d = [["A", "B", "C", "D", "E" ],
           ["1", "2", "3", "4", "5" ],
           ["a", "b", "c", "d", "e" ]]

# 가로 출력
for i in range(3):
    for j in range(5):
        print(f'list_2d([{i}][{j}]) = {list_2d[i][j]}', end=" ")
    print()

print("\n==========================================")
# 세로 출력
for i in range(5):
    for j in range(3):
        print(f'list_2d([{j}][{i}]) = {list_2d[j][i]}', end=" ")
    print()