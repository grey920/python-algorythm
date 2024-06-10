"""
https://www.acmicpc.net/problem/2441
오른쪽 정렬해서 점점 작아지는 별 출력
"""
n = int(input())

# for i in range(n):
#     for j in range(n):
#         if j >= i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

for i in range(n):
    print(" " * i + "*" * (n-i))