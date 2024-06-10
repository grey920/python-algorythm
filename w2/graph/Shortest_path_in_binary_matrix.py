from collections import deque


def shortestPathBinaryMatrix(grid):
    shortest_path_len = -1 # 도착하지 않는 경우의 리턴값으로 초기화
    row = len(grid)
    col = len(grid[0])

    # 시작지가 1 이거나 목적지가 1이면 바로 -1 리턴
    if grid[0][0] != 0 or grid[row-1][col-1] == 1:
        return shortest_path_len

    visited = [[False] * col for _ in range(row)]# 무한루프 방지 위해 방문 표시

    delta = [(1,0), (-1, 0), (0, 1), (0, -1),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # 목적지에 도착했을때 cur_len를 shortest_path_len로 저장 (목적지 좌표는 (row-1, col-1) )
        if cur_r == row -1 and cur_c == col-1:
            shortest_path_len = cur_len
            break

        # 연결된 정점 확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if 0 <= next_r < row and 0 <= next_c < col:
                if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len+1))
                    visited[next_r][next_c] = True

    return shortest_path_len



grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortestPathBinaryMatrix(grid))