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

def minKnightMoves( x: int, y: int) -> int:
    if x == 0 and y == 0: return 0
    visited = set()
    visited.add((0, 0))
    queue = deque([(0, 0, 0)])

    while queue:
        curx, cury, step = queue.popleft()
        if curx == x and cury == y:
            return step
        for i, j in [(2, 1), (1, 2), (2, -1), (-1, 2), (1, -2), (-2, 1), (-1, -2), (-2, -1)]:
            nx = i + curx
            ny = j + cury
            if (nx, ny) not in visited:
                queue.append((nx, ny, step + 1))
                visited.add((nx, ny))
    return -1
