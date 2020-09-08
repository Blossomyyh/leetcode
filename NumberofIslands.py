class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, vis):
        vis[i][j] = True

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and A[nRow][nCol] == '1' and not vis[nRow][nCol]:
                vis[nRow][nCol] = True
                self.dfs(A, nRow, nCol, vis)

    def numIslands(self,A):
        if not A: return 0
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j] == '1':
                    self.dfs(A,i,j,vis)
                    count += 1

        return count

Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0: return 0
        row = len(grid);
        col = len(grid[0])
        self.count = sum(grid[i][j] == '1' for i in range(row) for j in range(col))
        parent = [i for i in range(row * col)]

        def find(x):
            if parent[x] != x:
                return find(parent[x])
            return parent[x]

        def union(x, y):
            xroot, yroot = find(x), find(y)
            if xroot == yroot: return
            parent[xroot] = yroot
            self.count -= 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    continue
                index = i * col + j
                if j < col - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
                if i < row - 1 and grid[i + 1][j] == '1':
                    union(index, index + col)
        return self.count

# Approach : Using Union Find.
class Solution(object):

    # the number of islands using
    # Disjoint Set data structure.

    # Class to represent
    # Disjoint Set Data structure
    class DisjointUnionSets(object):
        def __init__(self, n):
            self.rank = [0] * n
            self.parent = [0] * n
            self.n = n
            self.makeSet()

        def makeSet(self):

            # Initially, all elements are in their
            # own set.
            for i in range(self.n):
                self.parent[i] = i

                # Finds the representative of the set that x

        # is an element of
        def find(self, x):
            if (self.parent[x] != x):
                # if x is not the parent of itself,
                # then x is not the representative of
                # its set.
                # so we recursively call Find on its parent
                # and move i's node directly under the
                # representative of this set
                return self.find(self.parent[x])
            return x

            # Unites the set that includes x and

        # the set that includes y
        def Union(self, x, y):

            # Find the representatives(or the root nodes)
            # for x an y
            xRoot = self.find(x)
            yRoot = self.find(y)

            # Elements are in the same set,
            # no need to unite anything.
            if xRoot == yRoot:
                return

            # If x's rank is less than y's rank
            # Then move x under y so that depth of tree
            # remains less
            if self.rank[xRoot] < self.rank[yRoot]:
                self.parent[xRoot] = yRoot

                # Else if y's rank is less than x's rank
            # Then move y under x so that depth of tree
            # remains less
            elif self.rank[yRoot] < self.rank[xRoot]:
                self.parent[yRoot] = xRoot

            else:

                # Else if their ranks are the same
                # Then move y under x (doesn't matter
                # which one goes where)
                self.parent[yRoot] = xRoot

                # And increment the result tree's
                # rank by 1
                self.rank[xRoot] = self.rank[xRoot] + 1

    # Returns number of islands in a[][]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])

        dus = self.DisjointUnionSets(rowCount * colCount)

        # The following loop checks for its neighbours
        # and unites the indexes if both are 1.
        for rowIdx in range(0, rowCount):
            for colIdx in range(0, colCount):

                # If cell is 0, nothing to do
                if grid[rowIdx][colIdx] == "0":
                    continue

                # Check all 4 neighbours and do a Union
                # with neighbour's set if neighbour is
                # also 1
                if rowIdx + 1 < rowCount and grid[rowIdx + 1][colIdx] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx + 1) * (colCount) + colIdx)

                if rowIdx - 1 >= 0 and grid[rowIdx - 1][colIdx] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx - 1) * (colCount) + colIdx)

                if colIdx + 1 < colCount and grid[rowIdx][colIdx + 1] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx) * (colCount) + colIdx + 1)

                if colIdx - 1 >= 0 and grid[rowIdx][colIdx - 1] == "1":
                    dus.Union(rowIdx * (colCount) + colIdx, (rowIdx) * (colCount) + colIdx - 1)

        # Array to note down frequency of each set
        frequencyArray = [0] * (rowCount * colCount)
        numberOfIslands = 0
        for rowIdx in range(rowCount):
            for colIdx in range(colCount):
                gridVal = grid[rowIdx][colIdx]
                if gridVal == "1":
                    x = dus.find(rowIdx * colCount + colIdx)

                    # If frequency of set is 0,
                    # increment numberOfIslands
                    if frequencyArray[x] == 0:
                        numberOfIslands += 1
                        frequencyArray[x] += 1
                    else:
                        frequencyArray[x] += 1
        return numberOfIslands



""" Number of closed islands """


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0

        # iterate through the grid from 1 to length og grid for rows
        # and columns.
        # the iteration starts from 1 because if a 0 is present
        # in the 0th column, it can't be a closed island.
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):

                # if the item in the grid is 0 and it is surrounded by
                # up, down, left, right 1's then increment the count.
                if grid[i][j] == 0 and self.dfs(grid, i, j):
                    count += 1
        return count

    def dfs(self, grid, i, j):

        # if grid[i][j] is 1 then return True, this helps is checking the
        # final return conditons.
        if grid[i][j] == 1:
            return True

        # now check if the element 0 is present at the outmost rows and column
        # then return False
        if i <= 0 or j <= 0 or i >= len(grid) - 1 or j >= len(grid[0]) - 1:
            return False

        # initialize the item as 1
        grid[i][j] = 1

        # now check the conditions for up, down, left, right
        up = self.dfs(grid, i + 1, j)
        down = self.dfs(grid, i - 1, j)
        right = self.dfs(grid, i, j + 1)
        left = self.dfs(grid, i, j - 1)

        # if up, down , left, right is True, then return to main function
        return up and down and left and right