class TicTacToe:
    """
    Record the number of moves for each rows, columns, and two diagonals.
For each move, we -1 for each player 1's move and +1 for player 2's move.
Then we just need to check whether any of the recored numbers equal to n or -n.

Excellent O(1) solution.
    """

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        # row[] record each sum of row
        # col[] ... col
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.antidiag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # p1-->-1, p2-->1

        offset = player * 2 - 3
        self.row[row] += offset
        self.col[col] += offset
        # diag
        if row==col:
            self.diag += offset
        # anti
        elif row +col == self.n -1:
            self.antidiag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.antidiag]:
            return 2
        elif -self.n in [self.row[row], self.col[col], self.diag, self.antidiag]:
            return 1
        return 0
