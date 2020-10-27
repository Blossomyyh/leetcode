def islandPerimeter(self, grid) -> int:
    r = len(grid)
    c = len(grid[0])
    res = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j]==1:
                res += 4
            if i>0 and grid[i-1][j]==1:
                res -=2
            if j>0 and grid[i][j-1]==1:
                res -=2
    return res