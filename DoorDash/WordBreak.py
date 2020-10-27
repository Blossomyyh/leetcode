class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False]*(len(s)+1)
        # dp[i] means s[:i+1] can be segmented into words in the wordDicts
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, len(s)):
                # dpi - true && substring(i-j+1) is next word
                if dp[i] and s[i:j+1] in wordDict:
                    dp[j+1] = True
        return dp[-1]