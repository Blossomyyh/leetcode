from collections import deque
def maxAreaOfIsland(self, grid) -> int:
    max_area = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = 0
                max_area = max(max_area, self.bfs(i, j, grid))
    return max_area


def bfs(self, i, j, grid):
    q = deque([(i, j)])
    area = 1
    while q:
        i, j = q.popleft()
        for I, J in [i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]:
            if 0 <= I < len(grid) and 0 <= J < len(grid[0]) and grid[I][J] == 1:
                grid[I][J] = 0
                q.append((I, J))
                area += 1
    return area