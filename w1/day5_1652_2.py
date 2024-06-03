"""
https://www.acmicpc.net/problem/1652
[문제분석]

"""
import sys


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


def main():
    input = sys.stdin.read
    data = input().split()

    room_size = int(data[0])
    room = [list(data[i + 1]) for i in range(room_size)]

    horizontal_spaces = count_horizontal_spaces(room, room_size)
    vertical_spaces = count_vertical_spaces(room, room_size)

    print(horizontal_spaces, vertical_spaces)


main()
