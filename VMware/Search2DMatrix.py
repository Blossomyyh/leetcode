"""
74. Search a 2D Matrix

binary search
O(logmn)
"""


def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or len(matrix[0]) == 0:
        return False
    row = len(matrix)
    col = len(matrix[0])
    s, e = 0, row * col - 1
    while s <= e:
        mid = (s + e) // 2
        r, c = divmod(mid, col)
        # quotient and remainder.

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            e = mid - 1
        else:
            s = mid + 1

    return False



"""
240. Search a 2D Matrix II

O(m+n)
anti-diagonal

\\ BottomLeft to TopRight
   can only 2 dir
\\ < target : go up
\\ >        : go right
"""


def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or len(matrix[0]) == 0: return False
    row = len(matrix)
    col = len(matrix[0])
    r, c = row - 1, 0
    while 0 <= r < row and 0 <= c < col:

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            c += 1
        else:
            r -= 1
    return False