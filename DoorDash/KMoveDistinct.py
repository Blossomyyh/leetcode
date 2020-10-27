def possiblePath(x,y, sx,sy, tx,ty, k):
    ans = 0
    dp = [[[1]*(k+1)]*y for _ in range(x)]

    def isValid(i,j):
        return 0<=i<x and 0<=j<y

    for s in range(2,k+1):
        """
        for every position (x,y) after
            // s number of steps
        """
        for i in range(x):
            for j in range(y):
                allsum = 0
                for ii,jj in [(1,0), (-1,0),(0,-1), (0,1), (1,1),(1,-1), (-1,1), (-1,-1) ]:
                    if isValid(i+ii, j+jj):
                        allsum+= dp[i+ii][j+jj][s-1]

                dp[i][j][s] = allsum
    print(dp[-1][-1])
    return dp[-1][-1][-1]

print(possiblePath(5,5,1,2,3,4,3))
