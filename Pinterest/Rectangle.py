# Rectangle
# 1. ⼀一个矩阵，只有0和1，找到⾥里里⾯面全为1的矩形的坐标。输⼊入⼀一定有效，保
# 证有⼀一个满⾜足要求的矩形。⽤用左上和右下坐标表示
# ⽐比如：
# 0 0 0 0 0. ⽜牛⼈人云集,⼀一亩三分地
# 0 1 1 0 0. more info on 1point3acres
# 00000
# 结果就是返回
#
# [1,1], [1,2]
#
# 2. follow up 有很多个这样的矩形， 返回所有的矩形的左上右下坐标
#
# 3. 不不⼀一定是矩形，找出所有连通的1. . from: 1point3acres
#
# 10011
#
# 00011
#
# 10001
#
# 这样的输⼊入，返回⼀一个⼤大数组
#
# [
#
# [0,0],
#
# [[0,3], [0,4], [1,3], [1,4], [2,4]],
#
# [2,1]
#
# ]

################################
"""
1. find the only rect in the matrix

traversal the matrix and find first 1:
    start from i,j
    go left find j -- check with 1
    then go down find i -- check with 1
    return start and end

Assumptions : valid input and only one rectangle to find,
time complexity : O(col*row)
Space complexity : O(1)
"""

test1 = [[0,0,0,0,0],
         [0,0,1,1,0],
         [0,0,1,1,0],
         [0,0,0,0,0]]

test2 = [[0,0,0,0,0],
         [0,0,1,1,0],
         [0,0,1,1,0],
         [1,1,0,0,0]]

test3 = [[1,0,0,1,1],
         [0,0,0,1,1],
         [1,0,0,0,1]]
def rectangleOne(matrix):
    row = len(matrix)
    col = len(matrix[0])
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                iBottom = i
                jRight = j
                # go right
                while 0<=jRight<col and matrix[i][jRight] == 1:
                    jRight += 1
                while 0<=iBottom<row and matrix[iBottom][j] == 1:
                    iBottom += 1
                return (i,j), (iBottom-1, jRight-1)

    return None, None
print(rectangleOne(test1))
# [(1, 2), (2, 3)]

"""
############################
2. find multiple rectangles
Assumption: no overlaps and valid input

traversal the matrix and find first 1:
    start from i,j
    go left find j -- check with 1
    then go down find i -- check with 1
    store start and end
    refill this rectangle with -1
time/space 
"""
def rectangleTwo(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result  = []

    def refill(i,j,iBottom, jRight):
        for iVar in range(i, iBottom+1):
            for jVar in range(j, jRight+1):
                matrix[iVar][jVar] = -1

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                iBottom = i
                jRight = j
                # go right
                while 0<=jRight<col and matrix[i][jRight] == 1:
                    jRight += 1
                while 0<=iBottom<row and matrix[iBottom][j] == 1:
                    iBottom += 1
                # topleft and bottomright
                """
                ######### take care of incrementation !!!!!!!
                need -1 for i, j !!!!!!!!!!
                """
                result.append([(i,j), (iBottom-1, jRight-1)])
                refill(i, j, iBottom-1, jRight-1)

    return result
print(rectangleTwo(test2))
# [[(1, 2), (2, 3)], [(3, 0), (3, 1)]]

"""
#############################
3. find all connected 1

DFS
traversal the matrix and find first 1:
    start from i,j
    go 4 dir: up down right left to find other 1 with DFS
        check valid and == 1
            mark -1
            start dfs for this new point again
    store list in result
time complexity: O(n*m, 2)
space complexity: O(1)
"""

"""
##################################################################
\\  permutation helper 
    \\ interation version
    def permutationHelper(self, nums, start=0):
        if start == len(nums) - 1:
            return [nums[:]]
        res = []
        for i in range(start, len(nums)):
            # self.swap(nums, start, i)
            nums[start], nums[i] = nums[i], nums[start]
            res += self.permutationHelper(nums, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
        return res
\\ not the same no add for 4 directions
"""
#################################
"""
\\ DFS helper for various path recording
If need record every path

1. start with []
2. append ele on the way
3. end with append this list
4. make list [] again
5. iterate

\\ different from permutation!
"""
#################################
def rectangleThree(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = []
    visited = set()

    def isValid(i, j):
        if 0<=i<row and 0<=j<col and matrix[i][j]==1 and (i,j) not in visited:
            return True
        return False

    def dfs(i, j):
        # mark visited
        visited.add((i,j))
        result.append((i,j))
        for iDir, jDir in [(1, 0), (-1, 0), (0,1), (0,-1)]:
            if isValid(i + iDir, j + jDir):
                dfs(i+iDir, j+jDir)

    result = []
    resultList = []
    for i in range(row):
        for j in range(col):
            if isValid(i, j):
                dfs(i,j)
                resultList.append(result)
                result = []

    return resultList
print(rectangleThree(test3))
# [[(0, 0)], [(0, 3), (1, 3), (0, 4), (1, 4), (2, 4)], [(2, 0)]]

"""
##########################
\\ BFS solution

"""
from collections import deque
def rectangleThreeB(matrix):
    row = len(matrix)
    col = len(matrix[0])
    visited = set()

    def isValid(i, j):
        if 0 <= i < row and 0 <= j < col and matrix[i][j] == 1 and (i,j) not in visited:
            return True
        return False

    queue = deque()
    resultList = []
    for i in range(row):
        for j in range(col):
            if isValid(i, j):
                path = []
                """
                \\ should add in set !!! at here
                """
                queue.append((i,j))
                visited.add((i,j))
                while queue:
                    curi, curj = queue.popleft()
                    path.append((curi, curj))
                    for iDir, jDir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        if isValid(curi + iDir, curj + jDir):
                            """
                                \\ should add in visited !!! at here
                                or before we append into path --> check whether already in set!!!!
                             """
                            visited.add((curi + iDir, curj + jDir))
                            queue.append((curi + iDir, curj + jDir))

                resultList.append(path)
    return resultList
print(rectangleThreeB(test3))






##################################################
def numIslands(grid):

    result = []
    connected_componet = []
    def dfs(grid, i, j):

        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':

            return
        grid[i][j] = '#'
        result.append([i,j])
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)

    if not grid:
        return 0


    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
                connected_componet.append(result)
                result = []
    return connected_componet

































