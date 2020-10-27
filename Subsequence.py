# Given a string s and a string t, check if s is subsequence of t.
"""
\\\\Two Pointer\\\\\\

len(s)>len(t) False
len(s)==0 True
len(t) False

searchpoint = 0
for each character in s:
    search t from searchpoint to find this character
    if not return False
    else:
        searchpoint to current index
return True

"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not t or len(s) > len(t): return False

        start = 0
        for ch in s:
            index = t.find(ch, start)
            if index == -1:
                return False
            else:
                start = index + 1
        return True


"""
\\Dynamic Programming
time S*T
"""

def isSubsequence(s: str, t: str) -> bool:
    sourceLen, targetLen = len(s), len(t)
    if sourceLen == 0:
        return True
    # never use []*xxx!!!!
    # copy itself!!!!
    # X -- dp = [[0]*(targetLen+1)]*(sourceLen+1)
    dp = [[0]*(targetLen+1) for _ in range(sourceLen + 1)]
    for i in range(1, sourceLen+1):
        for j in range(1,targetLen+1):
            # a match - dp[i-1][j-1]+1
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                # not match, inherit from left and downside
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(dp)
    """
      #   a  b  c  d  e    
    #[[0, 0, 0, 0, 0, 0],
    a[0, 1, 1, 1, 1, 1],
    c[0, 1, 1, 2, 2, 2], 
    e[0, 1, 1, 2, 2, 3]]
    """

    return dp[-1][-1] == sourceLen

print(isSubsequence("ace", "abcde"))