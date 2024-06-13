"""
백트래킹 예제
https://teamsparta.notion.site/12-2-922269f792db4e24aded633aa7383bf1
"""


def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
            return False
    return True


def solve_n_queens(board, row):
    n = len(board)
    if row == n:  #
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_n_queens(board, row + 1):
                return True
    return False


def print_board(board):
    n = len(board)
    for row in range(n):
        line = ['.'] * n
        line[board[row]] = 'Q'
        print(' '.join(line))


n = 8
board = [-1] * n
if solve_n_queens(board, 0):
    print_board(board)
else:
    print("No solution found")
