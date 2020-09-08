"""
48 medium

rotate the image by 90 degree clockwise
have to rotate the image in place, which means you should modify the input to the matrix not to allocate the other one

it is mostly about coding, it doesn't require too much in the area of algorithm or data structures
maybe some data structures in traversing those arrays
it's only has something to do with moving something around


If you take a look at this, I think one way you can do is :
 given the matrix
 first you transpose it so that you can sway X and Y coordinates, right?
 and you go through row by row and just reverse each item in the row

 it is sort of the series of the stuff that you can do , just playing around with the matrix


Another way to way to do this, is you just come up with a map,
you can go through each elements in the matrix and just map this stuff out
"""

from typing import List


class Solution:

    """simple : 1. transpose matrix 2. reverse matrix/each line"""
    def rotate1(self, matrix: List[List[int]]) -> None:
        l = len(matrix[0])

        for i in range(l):
            for j in range(i, l):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
        return matrix

    """
    matrix.reverse ---> upside down
    
    if wanna left to right --> matrix[j].reverse for j times
    
    """


    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or len(matrix) == 0: return matrix
        l = len(matrix[0])
        for i in range(l // 2 + l % 2):
            for j in range(l // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[l - j - 1][i]
                matrix[l - j - 1][i] = matrix[l - i - 1][l - j - 1]
                matrix[l - i - 1][l - j - 1] = matrix[j][l - i - 1]
                matrix[j][l - i - 1] = temp

        return matrix

"""
###### rotation ######:
keep line to col, make col to line and let it be (l-1-col) 
1. (i, j)
2. (l-j-1, i)
3. (l-i-1, l-j-1)
4. (j, l-i-1)

"""

m = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate1(m)