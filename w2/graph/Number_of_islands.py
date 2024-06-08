"""
https://leetcode.com/problems/number-of-islands/description/
- 그래프 -> DFS, BFS만 알아도 정답률 올라감
- 지도에 표시된 섬들의 총 갯수 반환
"""
from collections import deque


def numIslands(grid):
    number_of_islands = 0
    row = len(grid)
    col = len(grid[0])
    visited = [[False] * col for _ in range(row)]

    def bfs(x, y):
        # 상하좌우 방문방법 -> 외우기!!
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                # 방문할 수 있는 좌표: 좌표 밖을 벗어나지 않을때, 땅일때, 방문 안했을때
                if next_x >= 0 and next_x < row and next_y >= 0 and next_y < col:
                    if grid[next_x][next_y] == '1' and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == "1" and not visited[i][j]:
                bfs(i, j)
                number_of_islands += 1
    return number_of_islands


result = numIslands(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])

print(result)
