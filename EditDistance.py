# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

#  find the minimum number of operations required to convert word1 to word2.
#    h o r s e
#  0 1 2 3 4 5
# r1 1 2 2 3 4
# o2 2 1 2 3 4
# s3 3 2 2 2 3
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        if len1 * len2 == 0:
            return len1 + len2
        """init [*m for _in n] ---- [n][m]"""
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for j in range(len2 + 1):
            dp[0][j] = j
        for i in range(len1 + 1):
            dp[i][0] = i
        """"after init no need to go to line/column 0"""
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                leftdown = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else (dp[i - 1][j - 1] + 1)
                minstep = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, leftdown)
                dp[i][j] = minstep

        return dp[len1][len2]
