"""
In an infinite chess board with coordinates from -infinity to +infinity,
you have a knight at square [0, 0].

A knight has 8 possible moves it can make,as illustrated below.
 Each move is two squares in a cardinal direction,
 then one square in an orthogonal direction.
"""
"""
(0,0) (0,1)
(1,0) (1,1)

                (|x|,|y|) 
we can just focus on the matrix (0,0 )and end as (x,y)
make x,y position --> readable
i,j (0,1)

\\ use set to avoid redundancy
\\ shortest path --> BFS 
while queue :
    queue pop
    for each direction:
        append new node and its curr step in queue
        

"""
from collections import deque
def knight(x, y):
    if (x, y) == (0, 0): return 0

    def bfs(i, j, x, y):
        open_list = [(i, j, 0)]
        seen = {(i, j)}
        for i, j, d in open_list:
            for di, dj in [(1, 2), (2, 1), (1, -2), (2, -1),
                           (-1, 2), (-2, 1), (-1, -2), (-2, -1)]:
                r, c = i + di, j + dj
                if (r, c) not in seen and r > -4 and c > -4:
                    if (r, c) == (x, y): return d + 1
                    seen.add((r, c))
                    open_list.append((r, c, d + 1))

    return bfs(0, 0, abs(x), abs(y))
print(knight(5,5))
# 4



import collections

class Solution(object):
    def minKnightMoves(self, x:int, y:int):
        x, y = abs(x), abs(y)
        res = 0
        """
        optimization:
            best way to approach x,y
            go as far as we can 
            x>y go+(2,1)
            else (1,2)
        """

        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2
        # bfs
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
        queue = collections.deque([(0, 0, 0)])
        while queue:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return res + steps
            for di, dj in moves:
                if (x - i) * di > 0 or (y - j) * dj > 0: # move towards (x, y) at least in one direction
                    queue.append((i + di, j + dj, steps + 1))