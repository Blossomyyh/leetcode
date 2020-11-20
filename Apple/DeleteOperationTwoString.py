"""
583. Delete Operation for Two Strings


"""
def minDistance(word1: str, word2: str) -> int:
    l1 = len(word1)
    l2 = len(word2)
    dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

    # initialize dp -> delete i
    for i in range(l1 + 1):
        for j in range(l2 + 1):
            if j == 0 and i != 0:
                dp[i][0] = i
            elif i == 0 and j != 0:
                dp[0][j] = j
            elif j == 0 and i == 0:
                dp[i][j] = 0
            else:
                # compare ch in s1 and s2
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # not == need deletion
                    # find min on the left and top
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j]) + 1
    # for i in dp:
    #     print(i)
    return dp[-1][-1]