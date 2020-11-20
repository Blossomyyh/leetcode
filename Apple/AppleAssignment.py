"""
Input:
arr[ROW][COL]
Begin = {2, 4};
End = {8, 9};

Output:
Shortest Path is 13

Assumptions:
1. begin and end element can be either 1/0
2. arr can be edited

Solution:
1. check and modify input (invalid input will return -1)
2. use BFS to find shortest path
"""

from collections import deque
class Solution:
    def shortestRoute(self, arr: [[int]], begin: [int], end: [int]) -> int:
        # 1. check input
        #    check arr valid
        if not arr or not arr[0]:
            return -1

        row = len(arr)
        col = len(arr[0])

        #    check element valid and within range
        def checkValid(point):
            return 0 <= point[0] < row and 0 <= point[1] < col

        if not checkValid(begin) or not checkValid(end):
            return -1

        # 2. BFS to find shortest way
        queue = deque()
        begin.append(0)
        queue.append(begin)
        while queue:
            currow, curcol, path = queue.popleft()

            # base case
            # reach end point
            # the first way will be the shortest way
            if end == [currow, curcol]:
                return path

            # normal case
            # find 0 around current point
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if checkValid([currow + i, curcol + j]) and arr[currow + i][curcol + j] == 1:
                    # marked visited, count the updated path and add to queue
                    arr[currow + i][curcol + j] = -1
                    queue.append([currow + i, curcol + j, path + 1])

        return -1


if __name__ == "__main__":
    arr = [[1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
           [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 1, 1],
           [0, 0, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 1, 0, 0, 0, 0, 1, 1]]
    begin = [2, 4]
    end = [8, 9]
    shortest = Solution().shortestRoute(arr, end, begin)
    print("The shortest path : " + str(shortest))
    # The shortest path : 13
