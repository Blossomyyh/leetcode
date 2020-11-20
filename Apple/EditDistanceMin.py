"""
72. Edit Distance

"""
"""
always check 3 directions
left    dp[i][j - 1] + 1
up      dp[i - 1][j] + 1
leftup  dp[i - 1][j-1] (+1 if !=)
"""

def minDistance(self, word1: str, word2: str) -> int:
    len1 = len(word1)
    len2 = len(word2)

    # edge case
    if not len1 or not len2:
        if len1:
            return len2
        else:
            return len1

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        for j in range(len2 + 1):
            if j == 0:
                dp[i][j] = i
            elif i == 0 and j != 0:
                dp[i][j] = j
            else:
                left = dp[i][j - 1] + 1
                up = dp[i - 1][j] + 1
                leftup = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    leftup += 1
                    # left & up
                    # left-up -->
                dp[i][j] = min(left, up, leftup)
    for i in dp:
        print(i)
    return dp[-1][-1]