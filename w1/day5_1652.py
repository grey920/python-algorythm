"""
https://www.acmicpc.net/problem/1652
[문제분석]
- 2차원 배열로 변형
- 공간 카운트를 세다가 X를 만나면 초기화
- X 를 만나거나 행 순회가 끝나면 공간이 2 이상일때 최종 결과인 카운트 +1
"""
import sys


# 가로 탐색
def count_horizontal_spaces(room, size):
    row_space_count = 0
    for i in range(size):
        space = 0
        for j in range(size):
            if room[i][j] == 'X':
                if space >= 2:
                    row_space_count += 1
                space = 0
            else:
                space += 1

        # 마지막 열 처리
        if space >= 2:
            row_space_count += 1

    return row_space_count


# 세로 탐색
def count_vertical_spaces(room, size):
    col_space_count = 0
    for j in range(size):
        space = 0
        for i in range(size):
            if room[i][j] == 'X':
                if space >= 2:
                    col_space_count += 1
                space = 0
            else:
                space += 1

        # 마지막 행 처리
        if space >= 2:
            col_space_count += 1

    return col_space_count


# 입력을 모두 읽어 리스트로 변환
room_size = int(sys.stdin.readline())
room = [list(sys.stdin.readline().strip()) for _ in range(room_size)]

horizontal_cnt = count_horizontal_spaces(room, room_size)
vertical_cnt = count_vertical_spaces(room, room_size)

print(horizontal_cnt, vertical_cnt)
