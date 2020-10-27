"""  Treasure  """
# 0, -1 wall, 1 treasure
# 1. find all cell = 0 and no wall near
# 2. whether other 0 can reach (a,b)
# 3. given start and end, go through all treasures -- shortest path

'''
  1. whether cell no wall near

go through all the directions 
'''
test1 = [[0, 0, 0, 0, -1],
         [0, -1, -1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, -1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]


def treasure1(matrix, x, y):
    row = len(matrix)
    col = len(matrix[0])

    # check 4 directions
    def isValid(m, n):
        if 0 <= m < row and 0 <= n < col:
            return True
        return False

    for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        if isValid(i + x, j + y) and matrix[i + x][j + y]:
            return False
    return True


print(treasure1(test1, 5, 0))

'''
 2.  whether other 0 can reach (a,b)
 
Breadth First Search start at (a,b) & queue First in First out

traversal the matrix count all 0 -> total number 
 (corner case: no other 0, all 0 -true)
create a queue((a,b))
do BFS on (a,b)
do a while loop:
    get node from queue pop
    mark visited for this node
        go 4 directions to find other 0:
            append this point to queue
compare the count == visited?
    
'''
test2 = [[0, 0, 0, 0, -1],
         [0, -1, -1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, -1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, -1, 0, 0, 0]]

test4 = [[0, 0, 0, 0],
         [0, -1, 1, 0],
         [0, 0, 0, 0]]
from collections import deque
"""
Time complexity : O(mn). 
    We visit every square once
    Complete traversal of maze will be done in the worst case. 
    Here, mm and nn refers to the number of rows and coloumns of the maze

"""

def treasure2(matrix, a, b):
    if not matrix: return False
    row = len(matrix)
    col = len(matrix[0])

    def isValid(m, n):
        if 0 <= m < row and 0 <= n < col:
            return True
        return False

    count = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                count += 1
    if count == 1: return False
    if count == row * col: return True
    print(count)
    # BFS
    queue = deque()
    queue.append((a, b))
    visited = 0
    while queue and visited < count:
        curi, curj = queue.popleft()
        visited += 1
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if isValid(i + curi, j + curj) and matrix[i + curi][j + curj] == 0:
                queue.append((i + curi, j + curj))
    return visited == count
print(treasure2(test4, 2, 1))



'''
    3. given start and end, go through all treasures -- shortest path

go through matrix, creat a set for treasures
create queue(coordinates, visited treasure)
BFS from start point  
    queue pop to get coordinates, visited treasure
    
    if coordinates == end:
        if visited == treasures:
            return true
        else:
            continue
    
    go 4 direction 
        if next== 0 / 1 
            append this point, (+1 for visited if 1)
        
'''

test3 = [[0, 0, 0, 0, 0],
         [0, -1, -1, 0, 0],
         [0, -1, 0, 1, 0],
         [-1, 0, 0, 0, 0],
         [0, 1, -1, 0, 0],
         [0, 0, 0, 0, 0]]

def treasure3(matrix, start_x, start_y, end_x, end_y):
    if not matrix: return False
    row = len(matrix)
    col = len(matrix[0])

    def isValid(m, n):
        if 0 <= m < row and 0 <= n < col:
            return True
        return False

    treasure = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                treasure += 1
    print(treasure)

#     BFS
    queue = deque()
    visited  = set()
    if matrix[start_x][start_y] == 1:
        queue.append(([(start_x, start_y)], 1))
    else:
        queue.append(([(start_x, start_y)], 0))
    while queue:
        node= queue.popleft
        print(node)
        path = node[0]
        curT = node[1]
        print(path)
        curi, curj = path[-1]
        if curi == end_x and curj == end_y:
            if curT == treasure:
                return True
            else:
                continue
        visited.add((curi, curj))
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

            if isValid(i + curi, j + curj) and (i + curi, j + curj) not in visited:
                if matrix[i + curi][j + curj] == 0:
                    queue.append((path + [i + curi, j + curj], curT))
                    print(i + curi, j + curj, curT)
                elif matrix[i + curi][j + curj] == 1:
                    print(i + curi, j + curj, curT+1)
                    queue.append((path +[i + curi, j + curj], curT +1))
    return False

print(treasure3(test3, 5, 0, 0, 2))

























