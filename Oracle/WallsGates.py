"""
286. Walls and Gates
"""


def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]: return rooms
        row = len(rooms)
        col = len(rooms[0])

        def valid(i, j):
            return 0<=i<row and 0<=j<col

        def dfshelper(i, j, distance):
            if not valid(i,j) or rooms[i][j] < distance:
                return
            rooms[i][j] = distance
            for ii,jj in [(0,-1), (1,0), (-1,0), (0,1)]:
                dfshelper(ii+i,jj+j, distance+1)

        for i in range(row):
            for j in range(col):
                if rooms[i][j] ==0:
                    dfshelper(i,j, 0)
