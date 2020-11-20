"""
1091. Shortest Path in Binary Matrix
 8 directions

Time & space: O(n ^ 2), n = grid.length.
"""

from collections import deque
class Solution:
    """
    BFS

    """

    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        N, q, seen = len(grid), [(0, 0, 1)], set([0])
        for x, y, steps in q:
            if x == N - 1 and y == N - 1:
                return steps
            for i in (x - 1, x, x + 1):
                for j in (y - 1, y, y + 1):
                    if i >= 0 and i < N and j >= 0 and j < N and grid[i][j] == 0 and i * N + j not in seen:
                        seen.add(i * N + j)
                        q.append((i, j, steps + 1))
        return -1

    """
    DFS
    
    n DFS method, why are you checking for this condition --> Math.abs(d[x][y] - d[r][c]) > 1
A:
It's the recursion termination condition: 
distance values difference between any 2 neighboring non-blocked cells
 is no more than 1; 
 Specifically, if the difference <= 1, then the visiting cell maintains 
 the currently found shortest path distance value, 
 and there is no way to make the distance shorter.

For any 2 neighbors (x, y) and (r, c), 
if the difference between the distance from source (0, 0) is bigger than 1, e.g.,
 dist[x][y] = 3, dist[r][c] = 7, 
 then we can change the corresponding path of dist[r][c] to the corresponding path of dist[x][y] 
 plus the distance from (x, y) to its neighbor (r, c). 
 That is, updating dist[r][c] to the current shortest path distance: 
 dist[x][y] + 1 = 4
    """

    def shortestPathBinaryDFS(self, grid: [[int]]) -> int:
        if grid[0][0] or grid[-1][-1]:
            return -1
        N = len(grid)
        dist = [[float('inf')] * N for _ in range(N)]
        dist[0][0] = 1

        def dfs(grid: [[int]], dist: [[int]], x: int, y: int) -> None:
            for r in (x - 1, x, x + 1):
                for c in (y - 1, y, y + 1):
                    if r >= 0 and r < N and c >= 0 and c < N and grid[r][c] == 0 and abs(dist[x][y] - dist[r][c]) > 1:
                        if dist[x][y] > dist[r][c] + 1:
                            dist[x][y] = dist[r][c] + 1
                        else:
                            dist[r][c] = dist[x][y] + 1
                        dfs(grid, dist, r, c)

        dfs(grid, dist, 0, 0)
        print(dist)
        return dist[-1][-1] if dist[-1][-1] <= N * N else -1




    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        # 1. check input
        #    check arr valid
        arr = grid
        if not arr or not arr[0]:
            return -1

        row = len(arr)
        col = len(arr[0])
        begin = [0, 0]
        end = [row - 1, col - 1]

        #    check element valid and within range
        def checkValid(point):
            return 0 <= point[0] < row and 0 <= point[1] < col

        if not checkValid(begin) or not checkValid(end) or grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # 2. BFS to find shortest way
        queue = deque()
        begin.append(1)
        queue.append(begin)
        while queue:
            currow, curcol, path = queue.popleft()

            # base case
            # reach end point
            # the first way will be the shortest way
            if end == [currow, curcol]:
                return path

            # normal case
            # find 0 around current point
            for i, j in [(1, 0), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if checkValid([currow + i, curcol + j]) and arr[currow + i][curcol + j] == 0:
                    # marked visited, count the updated path and add to queue
                    arr[currow + i][curcol + j] = -1
                    queue.append([currow + i, curcol + j, path + 1])

        return -1

Solution().shortestPathBinaryDFS([[0,0,0],[1,1,0],[1,1,0]])