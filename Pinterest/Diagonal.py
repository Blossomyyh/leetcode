"""


antidiagonal
diagonal

use direction to record
horizontally diagonally
    for i from 0 to col-1:
        linelist = []
            tp1 = i, j =0
            while until meet the end
        if dir == 1:
        if dir == -1:
            reverse the linelist \\ (2, 0) (1,1) (0,2)
        dir = -dir

next part: deal with vertical
"""
from typing import List

def findDiagonalOrder(matrix: List[List[int]]) -> List[int]:
    if not matrix: return []
    row = len(matrix)
    col = len(matrix[0])
    if col==row==1: return matrix
    result = []

    # go up at first
    direction = 1
    # horizontal part
    for j in range(0, col):
        tempj, i= j, 0
        linelist = []
        while 0<=tempj<col and 0<=i<row:
            linelist.append(matrix[i][tempj])
            tempj -= 1
            i += 1
        if direction == 1:
            result += linelist[::-1]
        else:
            result += linelist
        print(linelist)
        direction  = -direction

    # vertical (1, col-1), (row-1, col-1)
    for i in range(1, row):
        tempi, j  = i, col-1
        linelist = []
        while 0<=tempi<row and 0<=j<col:
            linelist.append(matrix[tempi][j])
            tempi += 1
            j -= 1
        if direction == 1:
            result += linelist[::-1]
        else:
            result += linelist
        direction  = -direction
        print(linelist)

    return result

# test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
# print(findDiagonalOrder(test))


def findDiagonalOrderLeft(matrix: List[List[int]]) -> List[int]:
    if not matrix: return []
    row = len(matrix)
    col = len(matrix[0])
    if col==row==1: return matrix
    result = []

    # go up at first
    direction = -1
    # horizontal part
    for j in range(0, col):
        tempj, i= j, row -1
        linelist = []
        while 0<=tempj<col and 0<=i<row:
            linelist.append(matrix[i][tempj])
            tempj -= 1
            i -= 1
        if direction == -1:
            result += linelist[::-1]
        else:
            result += linelist
        print(linelist)
        direction  = -direction

    # vertical (1, col-1), (row-1, col-1)
    """""""""
    REMEBER TO RANGE(  X, X  , -1 ) 
     
     -1 FOR REVERSELY
    
    """
    for i in range(row -2, -1, -1):
        tempi, j  = i, col-1
        linelist = []
        while 0<=tempi<row and 0<=j<col:
            linelist.append(matrix[tempi][j])
            tempi -= 1
            j -= 1
        if direction == -1:
            result += linelist[::-1]
        else:
            result += linelist
        direction  = -direction
        print(linelist)

    return result

test = [[1,2,3,4],[5,6,7,8],[9,10,11,12],]
print(findDiagonalOrderLeft(test))
