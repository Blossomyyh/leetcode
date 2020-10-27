def updateMatrix(self, matrix):
    """
    Python3 solution with only O(1) space complexity.
Scan twice from top-left and bottom-right separately.
We simply do 2 iterations from first to last and last to first element.
For the 1st for loop, we update distance of element with minimum of previous top and left elements + 1 (itself).
For the 2nd for loop, we update distance of element with minimum of previous bottom and right elements + 1 (itself).
As a result, we get minimum distance value for each element updated with distances of neighbours + 1.
    """
    m, n = len(matrix), len(matrix[0])
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell:
                top = matrix[i - 1][j] if i else float('inf')
                left = matrix[i][j - 1] if j else float('inf')
                matrix[i][j] = min(top, left) + 1
    for i in reversed(range(m)):
        for j in reversed(range(n)):
            if cell:
                bottom = matrix[i + 1][j] if i < m - 1 else float('inf')
                right = matrix[i][j + 1] if j < n - 1 else float('inf')
                matrix[i][j] = min(cell, bottom + 1, right + 1)


    return matrix


"""BFS"""


def updateMatrix(self, matrix):
    # BFS helper #
    def bfs(node):
        from collections import deque
        q = deque()
        i, j = node
        q.append(((i, j), 0))  # d (dist to a zero) = 0 initially
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for i in range(len(q)):
                coor, d = q.popleft()
                x, y = coor
                # if a zero nei is found
                if matrix[x][y] == 0:
                    return d
                visited.add(coor)
                # investiagte neighbours
                for dir in dirs:
                    newX, newY = x + dir[0], y + dir[1]
                    # within bounds:
                    if newX >= 0 and newX <= len(matrix) - 1 and \
                                    newY >= 0 and newY <= len(matrix[0]) - 1:
                        # not seen:
                        if (newX, newY) not in visited:
                            q.append(((newX, newY), d + 1))
        return -1

        # main logic #
        '''
        steps:
            - itertate over matrix to find cells = 1
            - pass cells equaling 1 to a bfs to find the closest 0 to them
            - update matrix
        '''


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                d = bfs((i, j))  # d = closest dist to a 0
                matrix[i][j] = d  # update M with d
    return matrix