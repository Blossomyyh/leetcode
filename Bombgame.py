'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each 1 cell.
The distance between two adjacent cells is 1.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.

case 1 :

[[0,0,0],
 [0,1,0],
 [0,0,0]]

[[0,0,0],
 [0,1,0],
 [0,0,0]]

case 2:

[[0,1,0],
 [1,1,1],
 [1,2,1]]

[[0,0,0],
 [0,1,0],
 [1,2,1]]

 (2,1) -- 4 direction: dfs to search 0
case 3:

[[0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
traversal the matrix find 1:
  queue FIFO
  do BFS for i,j:
    go 4 direction:
       append((i,j), distance)
  replace distance
'''

matrix = [[0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]
from collections import deque
def findDistance(matrix):
  row = len(matrix)
  col = len(matrix[0])

  def bfs(i, j):
    minDis = float('inf')
        # get the shortest path for top and left dir
    queue  = deque()
    queue.append([(i,j), 0])
    while queue:
      node, num = queue.popleft()
      i, j = node
      print(node, num)
      for iDir, jDir in [(0, -1),(-1, 0), (1,0), (0,1)]:
        if 0<=i+iDir<row and 0<=j+jDir<col and matrix[i+iDir][j+jDir] == 0:
          return  num+1
        elif 0<=i+iDir<row and 0<=j+jDir<col and matrix[i+iDir][j+jDir] >= 1:
          queue.append([(i+iDir, j+jDir), num+1])
          print(queue)
    return
  for i in range(row):
    for j in range(col):
      if matrix[i][j] == 1:
        matrix[i][j] = bfs(i,j)

  return matrix
print(findDistance(matrix))

  # time m*n*2^(mn)
  #  O(mn)