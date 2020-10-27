'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

matrix = [[1,1,1],
          [1,1,0],
          [1,0,1]]
starting_pixel = [1, 1]
newColor = 2
output = [[2,2,2],
          [2,2,0],
          [2,0,1]]
          2 - [-2]
start dfs from start point
  find similar color -> turn to new one
  go through all possible pixes
time O(M*N)
space O(M*N)
heap - malloc
stack - store variables in fuctions, record function address
'''


def floodfill(matrix, i, j, newColor):
    if not matrix or not matrix[0]:
        return matrix
    row = len(matrix)
    col = len(matrix[0])

    def isValid(m, n):
        if 0 <= m < row and 0 <= n < col:
            return True
        return False

    stack = []
    if not isValid(i, j):
        return []
    original = matrix[i][j]
    matrix[i][j] = newColor
    stack.append([i, j, original])
    while stack:
        si, sj, original = stack.pop()
        for ii, jj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if isValid(si + ii, sj + jj) and matrix[si + ii][sj + jj] == original:
                matrix[si + ii][sj + jj] = newColor
                stack.append([si + ii, sj + jj, original])
    return matrix


matrix = [[4, 4, 4],
          [4, 4, 0],
          [4, 0, 1]]
# matrix = [[]]
print(floodfill(matrix, 1, 1, 3))
