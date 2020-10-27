

"""
505. The Maze II


store distance in a matrix
go bfs for all solutions
when a distance of next cell can be update(be less) then append into queue

"""
'''
\\ solution 1 BFS
\\ solution 2 Dijkstra --> Heapq
'''

from typing import List
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze:
            return False
        row = len(maze)
        col = len(maze[0])
        distance = [[float('inf') ] *col for _ in range(row)]
        # check 4 directions
        def isValid(m, n):
            if 0 <= m < row and 0 <= n < col:
                return True
            return False
        queue = deque()
        queue.append((start[0], start[1]))
        distance[start[0]][start[1] ] =0
        # visited = set()
        while queue:
            curx, cury = queue.popleft()
            # distance[curx][cury] = min(distance[curx][cury], path)
            if curx == destination[0] and cury== destination[1]:
                continue
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextx, nexty, pathupdate = curx + i, cury + j, 0
                while isValid(nextx, nexty) and maze[nextx][nexty] == 0:
                    pathupdate += 1
                    nextx, nexty = nextx + i, nexty + j
                nextx, nexty = nextx - i, nexty - j
                print(distance[curx][cury], pathupdate, distance[nextx][nexty])
                if distance[curx][cury] + pathupdate < distance[nextx][nexty]:
                    distance[nextx][nexty] = distance[curx][cury] + pathupdate
                    queue.append((nextx, nexty))
                    # print(distance)
        return distance[destination[0]][destination[1]] if distance[destination[0]][destination[1]] != float(
            'inf') else -1
"""
Time complexity : 
O(m*n*max(m,n))O(m∗n∗max(m,n)). 
Time complexity O(m∗n∗max(m,n)).
 Complete traversal of maze will be done in the worst case. 
 Here, mm and nn refers to the number of rows and columns of the maze. 
 Further, for every current node chosen, we can travel upto a maximum depth of
  \text{max}(m,n)max(m,n) in any direction.

Space complexity : O(mn). 
queuequeue size can grow upto m*n in the worst case.
"""

"""
\\ 2
store all visited node and its distance in a heap
dictionary to record all visited distance for a node
pop out the min distance each time
if  == destination return path
go bfs for all paths
when a distance of next cell can be update(be less) - compare with previous one in dictionary
then append into queue


\\ worst m*n*log(m*n)

"""
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not maze:
            return False
        row = len(maze)
        col = len(maze[0])
        heap = []

        # check 4 directions
        def isValid(m, n):
            if 0 <= m < row and 0 <= n < col:
                return True
            return False

        heapq.heappush(heap, (0, start[0], start[1]))
        visited = {(start[0], start[1]): 0}

        while heap:
            dis, curx, cury = heapq.heappop(heap)

            # distance[curx][cury] = min(distance[curx][cury], path)
            if curx == destination[0] and cury == destination[1]:
                return dis
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextx, nexty, pathupdate = curx + i, cury + j, 0
                while isValid(nextx, nexty) and maze[nextx][nexty] == 0:
                    pathupdate += 1
                    nextx, nexty = nextx + i, nexty + j
                nextx, nexty = nextx - i, nexty - j
                if (nextx, nexty) not in visited or visited[(nextx, nexty)] > pathupdate + dis:
                    # print(nextx, nexty, pathupdate+dis)
                    visited[(nextx, nexty)] = pathupdate + dis
                    heapq.heappush(heap, (pathupdate + dis, nextx, nexty))
                    # print(visited)

                    # print(distance)
        return -1


"""
\\ 490. The Maze

0010s
00000
11011
0000e

BFS finds the shortest path first and essentially tries to visit all the vertices reachable from a given source vertex. 
But DFS focuses on discovering all edges.
DFS goes as deep as you can first. BFS visits neighbour nodes first.

queue to store all next nodes
use set to record visited nodes
while loop when queue is not empty
    get node from queue
    add node to set
    if node == end：
        return True
    try 4 directions & add to queue if possible and not visited
return False

"""
from collections import deque


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze:
            return False
        row = len(maze)
        col = len(maze[0])

        # check 4 directions
        def isValid(m, n):
            if 0 <= m < row and 0 <= n < col:
                return True
            return False

        queue = deque()
        queue.append((start[0], start[1]))
        # visited = set()
        while queue:
            curx, cury = queue.popleft()
            if curx == destination[0] and cury == destination[1]:
                return True
            # visited.add((curx, cury))
            maze[curx][cury] = -1
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nextx, nexty = curx + i, cury + j
                while isValid(nextx, nexty) and maze[nextx][nexty] != 1:
                    nextx, nexty = nextx + i, nexty + j
                nextx, nexty = nextx - i, nexty - j
                if maze[nextx][nexty] == 0:
                    queue.append((nextx, nexty))
        return False


