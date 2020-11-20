"""
Connect 4
use get column and line and diagonals to find wins
4 ->wins

https://codereview.stackexchange.com/questions/225840/a-simple-connect-4-game-in-python
https://github.com/KeithGalli/Connect4-Python/blob/master/connect4.py

Better solution:

focus on the current move's row and col! to check wins

"""
TEAM1 = 1
TEAM2 = 2

class connect4:
    def __init__(self, row=6, col=7):
        self.row = row
        self.col = col
        # generate empty 6*6 board
        self.board = [[0]*self.col for _ in range(self.row)]
        self.rows =[]
        self.count = self.row * self.col
        # one situation- 4positions  -> 0; team1+1, team2-1  4/-4--> win

    def returnboard(self):
        for i in range(self.row):
            print(self.board[i])
        return

    def checkwins(self, team):
        # n*m --> Time O(4*N*M)
        # horizontally
        for r in range(self.row):
            for c in range(self.col - 3):
                if self.board[r][c] == team and self.board[r][c+1]== team and self.board[r][c+2]== team and self.board[r][c+3]== team:
                    return True

        # vertically
        for r in range(self.row - 3):
            for c in range(self.col):
                if self.board[r][c] == team and self.board[r+1][c] == team and self.board[r+2][c] == team and self.board[r+3][c] == team:
                    return True

        # diagonally
        for r in range(self.row -3):
            for c in range(self.col - 3):
                if self.board[r][c] == team and self.board[r+1][c+1]== team and self.board[r+2][c+2]== team and self.board[r+3][c+3] == team:
                    return True

        # anti-diagonally
        for r in range(3, self.row):
            for c in range(self.col - 3):
                if self.board[r][c] == team and self.board[r-1][c+1] == team and self.board[r-2][c+2] == team and self.board[r-3][c+3] == team:
                    return True
        return False

    def checkcolumn(self, col):
        # check whether the current column can make move
        return 0 in [i[col] for i in self.board]

    def checkend(self, rounds):
        # check all the element are filled
        print("The end of the game! ")
        return rounds > self.count

    def makemove(self, team, col):
        # col is valid here
        i = self.row -1
        # check from bottom until find the empty position
        while self.board[i][col] != 0:
            i -= 1
        self.board[i][col] = team
        print(str(team)+" move at col: " +str(col))
        self.returnboard()
        if self.checkwins(team):
            print("Team "+str(team)+ " WIN !")
            return True

        return False


import random
if __name__ == "__main__":
    game = connect4()
    game.returnboard()
    rounds = 1
    win = False
    while not win and not game.checkend(rounds):

        team = rounds % 2 + 1
        # generate a random number 0-6
        colidx = random.randrange(7)
        while not game.checkcolumn(colidx):
            colidx = random.randrange(7)
        win = game.makemove(team, colidx)
        rounds += 1
    game.returnboard()







