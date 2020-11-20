"""
54. Spiral Matrix

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3


class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        def getDir(d):
            if d == RIGHT:
                return DOWN
            elif d == DOWN:
                return LEFT
            elif d == LEFT:
                return UP
            elif d == UP:
                return RIGHT

        def getNextPos(d, x, y):
            if d == RIGHT:
                return x, y + 1
            elif d == DOWN:
                return x + 1, y
            elif d == LEFT:
                return x, y - 1
            elif d == UP:
                return x - 1, y

        def valid(x, y):
            return 0 <= x < row and 0 <= y < col and matrix[x][y]

        res = []
        if not matrix or not matrix[0]:
            return []
        # visited = set()
        row = len(matrix)
        col = len(matrix[0])
        count = row * col
        x, y, d = 0, 0, 0
        while count:

            res.append(matrix[x][y])

            """ mark visited as None !!"""
            matrix[x][y] = None
            count -= 1
            nx, ny = getNextPos(d, x, y)
            # print(nx, ny, valid(nx, ny))
            if not valid(nx, ny):
                d = getDir(d)
                x, y = getNextPos(d, x, y)
            else:
                x, y = getNextPos(d, x, y)

        return res