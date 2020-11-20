"""
773. Sliding Puzzle
Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
and an empty square represented by 0.
A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
Input: board = [[4,1,2],
                [5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],
              [5,0,3]]
After move 1: [[4,1,2],
               [0,5,3]]
After move 2: [[0,1,2],
               [4,5,3]]
After move 3: [[1,0,2],
               [4,5,3]]
After move 4: [[1,2,0],
               [4,5,3]]
After move 5: [[1,2,3],
               [4,5,0]]
"""
"""
BFS find shortest 
    check end:
        string to compare X traversal board
transfer board -> string
"""
from collections import deque
def slidingPuzzle(board: [[int]]) -> int:

    start = ''.join(str(d) for row in board for d in row)
    # "412503"
    queue = deque()
    seen = set() # seen append start status
    queue.append((start, start.index('0')))
    step = 0
    row = len(board)
    col = len(board[0])
    def checkvalid(i,j):
        return 0<=i<len(board) and 0<=j<len(board[0])

    while queue:
        # get next status level by level
        nextlevel = deque()

        for i in range(len(queue)):
            # get current status and idx of 0
            cur, curidx = queue.popleft()
            seen.add(cur)
            # base case
            if cur == '123450':
                return step
            # cal x, y in board
            x = curidx // col
            y = curidx % col
            # go 4-directionally adjacent number and swapping it
            for i, j in [(0, 1), (1, 0),(-1, 0), (0, -1)]:
                if checkvalid(x+i, y+j):
                    currow = x+i
                    curcol = y+j
                    # string is unmutable
                    characters = [d for d in cur]
                    characters[curidx], characters[currow* col + curcol] = characters[currow* col + curcol], '0'
                    nextstate = ''.join(characters)

                    # check whether in seen
                    if nextstate not in seen:
                        nextlevel.append((nextstate, currow* col + curcol))
        step += 1
        queue = nextlevel

    return -1


