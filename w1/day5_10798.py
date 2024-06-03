"""
https://www.acmicpc.net/problem/10798
[문제분석]
- 행과 열을 바꾸기
"""
import sys

"""입력받은 문자열을 저장할 2차원 배열 생성"""
words = [["*" for i in range(15)] for j in range(5)]
for i in range(5):
    word = sys.stdin.readline().rstrip()
    for j in range(len(word)):
        words[i][j] = word[j]

# 2차원 배열의 열의 최대 크기
for i in range(15):
    # 2차원 배열의 행의 크기
    for j in range(5):
        if words[j][i] != "*":
            print(words[j][i], end="")
