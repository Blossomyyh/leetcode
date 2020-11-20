"""
317. Shortest Distance from All Buildings

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7

BFS --> pruning
calculate buildings, obstacles, way
distSum
    record the sum of distance from all 1 grids to this 0 grid.
hit
    record how many times a 0 grid has been reached
for each 1 --> find the 0 it can reach and record the dis
for each 0 has hit building times
    find the minimum sum distance
"""
from collections import deque
def shortestDistance(grid: [[int]]) -> int:
    # edge cases
    if not grid and not grid[0]: return -1
    row = len(grid)
    col = len(grid[0])
    building, obstacle, way = 0, 0, 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                building += 1
            elif grid[i][j] == 2:
                obstacle += 1
            elif grid[i][j] == 0:
                way += 1
    """remember hit and sumdistance in a cell"""
    hit = [[0]*col for _ in range(row)]
    # Use hit \\ to record how many times a 0 grid has been reached
    sumdis = [[0]*col for _ in range(row)]

    # bfs start at (x, y) -- queue to traversal
    # return True/False
    def valid(x, y):
        return 0<=x<row and 0<=y<col
    def bfs(x, y):
        queue = deque()
        queue.append((x,y, 0))
        visited = set()
        visited.add((x,y))
        count = 1
        while queue:
            curx, cury, curdis = queue.popleft()
            for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if valid(curx+i, cury+j) and (curx+i, cury+j) not in visited:
                    visited.add((curx+i, cury+j))
                    if grid[curx+i][cury+j] == 0:

                        queue.append((curx+i, cury+j, curdis + 1))
                        hit[curx+i][cury+j] += 1
                        sumdis[curx+i][cury+j] += curdis + 1

                    elif grid[curx+i][cury+j] == 1:
                        count += 1
                        """A powerful pruning is that during the BFS 
                        we use count1 to count how many 1 grids we reached"""
        return count == building

    for x in range(row):
        for y in range(col):
            if grid[x][y]==1:
                if not bfs(x,y):
                    return -1
    """check when hit == building & min of this sumdis"""
    res = float('inf')
    for x in range(row):
        for y in range(col):
            if hit[x][y]==building:
                res = min(res, sumdis[x][y])

    return res if res != float('inf') else -1

grid = [[1,0,2,0,1],
        [0,0,0,0,0],
        [0,0,1,0,0]]

grid = [[1]] # -1
print(shortestDistance(grid))
# def shortestDistance(self, grid):
#     if not grid or not grid[0]: return -1
#     M, N, buildings = len(grid), len(grid[0]), sum(val for line in grid for val in line if val == 1)
#     hit, distSum = [[0] * N for i in range(M)], [[0] * N for i in range(M)]
#
#     def BFS(start_x, start_y):
#         visited = [[False] * N for k in range(M)]
#         visited[start_x][start_y], count1, queue = True, 1, collections.deque([(start_x, start_y, 0)])
#         while queue:
#             x, y, dist = queue.popleft()
#             for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
#                 if 0 <= i < M and 0 <= j < N and not visited[i][j]:
#                     visited[i][j] = True
#                     if not grid[i][j]:
#                         queue.append((i, j, dist + 1))
#                         hit[i][j] += 1
#                         distSum[i][j] += dist + 1
#                     elif grid[i][j] == 1:
#                         count1 += 1
#         return count1 == buildings
#
#     for x in range(M):
#         for y in range(N):
#             if grid[x][y] == 1:
#                 if not BFS(x, y): return -1
#     return min([distSum[i][j] for i in range(M) for j in range(N) if not grid[i][j] and hit[i][j] == buildings] or [-1])