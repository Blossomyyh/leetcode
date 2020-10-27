"""

63. Unique Paths II
"""

def uniquePathsWithObstacles(self, obstacleGrid) -> int:
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    """corner case:  [[0]] - 1   [[1]] --0"""
    """corner case: [[0, 1]]"""
    if not obstacleGrid or len(obstacleGrid[0]) == 0:
        return 0

    dp = [[0] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if (i == 0 or j == 0) and obstacleGrid[i][j] != 1:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
    return dp[-1][-1]
