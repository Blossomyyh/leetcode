"""
36. Valid Sudoku

check 9 subboard
9 col
9 row
2 diagonals
"""
def isValidSudoku(self, board: [[str]]) -> bool:
    subboard = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    rows = [set() for _ in range(9)]
    diagonal = set()
    antidia = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            ele = board[i][j]
            if ele !='.':
                boardidx = (i// 3) * 3+j//3
                if ele not in subboard[boardidx]:
                    subboard[boardidx].add(ele)
                else:
                    return False
                if ele not in cols[j]:
                    cols[j].add(ele)
                else:
                    return False
                if ele not in rows[i]:
                    rows[i].add(ele)
                else:
                    return False
    return True

def valid(board):
    subboard = [{} for _ in range(9)]
    cols = [{} for _ in range(9)]
    rows = [{} for _ in range(9)]

    for i in range(len(board)):
        for j in range(len(board[0])):
            ele = board[i][j]
            if ele != '.':
                boardidx = (i // 3) * 3 + j // 3
                subboard[boardidx][ele] = subboard[boardidx].get(ele, 0) +1
                rows[i][ele] = rows[i].get(ele, 0) + 1
                cols[j][ele] = cols[j].get(ele, 0) + 1
                if subboard[boardidx][ele]>1 or rows[i][ele]>1 or cols[j][ele]>1:
                    return False
    return True


"""

"""


class Solution:
    def solveSudoku(self, board: [[str]]) -> None:
        n = len(board)
        # 3*9 sets
        subboard = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        rows = [set() for _ in range(n)]

        def isValid(r, c, v):
            idx = getidx(r, c)
            return v not in subboard[idx] and v not in rows[r] and v not in cols[c]

        def getidx(r, c):
            return (r // 3) * 3 + c // 3

        # preprocessing board
        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                else:
                    num = int(board[r][c])
                    idx = getidx(r, c)
                    subboard[idx].add(num)
                    cols[c].add(num)
                    rows[r].add(num)

        # print(subboard)
        # print(cols)
        # print(rows)
        # use backtracking to solve sudoku
        def backtrack(r, c):
            # base - all filled with r-n-1,c-n
            if r == n - 1 and c == n:
                return True
            elif c == n:
                c = 0
                r += 1
            # if filled, get next one
            if board[r][c] != '.':
                return backtrack(r, c + 1)

            # fill with valid number
            for v in range(1, n + 1):
                if not isValid(r, c, v):
                    continue

                idx = getidx(r, c)
                board[r][c] = str(v)
                rows[r].add(v)
                cols[c].add(v)
                subboard[idx].add(v)

                if backtrack(r, c + 1):
                    return True
                    # delete v
                board[r][c] = '.'
                rows[r].remove(v)
                cols[c].remove(v)
                subboard[idx].remove(v)

            return False

        backtrack(0, 0)

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
for i in board:
    print(i)

"""
sol 2
"""
class Solution:
    def solveSudoku(self, board):
        self.board = board
        self.solve()
        n = 9
        self.subboard = [set() for _ in range(n)]
        self.cols = [set() for _ in range(n)]
        self.rows = [set() for _ in range(n)]

    def solve(self):  # 主递归函数
        """preprocess"""

        row, col = self.ﬁndUnassigned()  # 获取⼀一个未被分配的⽅方格
        if row == -1 and col == -1:  # 没有找到，说明已经填好
            return True

        for num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.isSafe(row, col, num):  # 循环填⼊入数字，并判断是否满⾜足要求
                self.board[row][col] = num
                # subboard[idx].add(num)
                # cols[c].add(num)
                # rows[r].add(num)

                if self.solve():  # 递归进⼊入下⼀一个⽅方格
                    return True

                self.board[row][col] = '.'  # 后续不不满⾜足，那么现在要回复当前环境，并进⾏行行下⼀一个数字

        return False



    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '.':
                    return row, col
        return -1, -1

    def isSafe(self, r, c, v):
        idx = (r // 3) * 3 + c // 3
        return v not in self.subboard[idx] and v not in self.rows[r] and v not in self.cols[c]


