"""
62. Unique Paths
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""

"""
Dynamic programming

d[col][row] = d[col - 1][row] + d[col][row - 1].
 m = 3, n - 4
 
 0 1 1  1  1
 1 2 3  4  5
 1 3 6 10 15
 1 4 10 2035
 
To such cell one could move either from the upper cell (m, n - 1), 
or from the cell on the right (m - 1, n). 
That means that the total number of paths to move into (m, n) cell 
is uniquePaths(m - 1, n) + uniquePaths(m, n - 1).
"""


def uniquePaths(self, m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[-1][-1]






######
# recursive sol
def uniquePaths(self, m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    else:
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
"""

Math: m+n len get m-1 as horizontal, n-1 as vertical
(since we are at 0,0)
C(h+v h)-- (m+n-2)!/((m-1)!(n-1)!)
"""

from math import factorial
def uniquePaths(self, m: int, n: int) -> int:
    return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)