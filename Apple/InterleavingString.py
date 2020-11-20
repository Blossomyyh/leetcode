"""
97. Interleaving String

 s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
"""

"""
\\ DP 
i0 d b b c a   j
0T F F F F F
aT F F F F F
aT T T T T F
bF T T F T F
cF F T T T T
cF F F T F T

a a d b b c b c a c
index - i+j-1

for i, j 
    \\ dp[i][j-1] - T check  s2[j - 1] == s3[i + j - 1]
        second last one is ok, last one be s2[j - 1] 
    \\ dp[i-1][j] - T check  
"""


def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            elif i == 0 and j != 0:
                dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            elif j == 0 and i != 0:
                dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            else:
                dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
    for i in dp:
        print(i)

    return dp[-1][-1]

