from typing import List
"""
给每个user访问历史记录，找出两个user之间longest continuous common history 
输入： [ 

["3234.html", "xys.html", "7hsaa.html"], // user1 

["3234.html", ''sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2 

], user1 and user2 （指定两个user求intersect）   

 输出：["xys.html", "7hsaa.html"]
 
 \\Dynamic programming
 
 user1 : 9,4,6,7,1
 user2: 9,2,3,4,6,7
 maxpoint 4,6
 
  # 9,2,3,4,6,7
 #0 0 0 0 0 0 0
 90 1 0 0 0 0 
 40 0 0 0 1 0 
 60 0 0 0 0 2
 70 0 0 0 0 0 3
 10 0 0 0 0

"""


def longestCommonHistory(user1, user2):
    if not user1 or not user2:
        return []
    result = []
    row = len(user1)
    col = len(user2)

    dp = [[0]*(col +1) for _ in range(row + 1)]
    print(dp)
    maxLength = 0
    maxPoint = (0, 0)
    for i in range(1, row+1):
        for j in range(1, col +1):
            if user1[i-1] == user2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

                if dp[i][j]>maxLength:
                    maxLength = dp[i][j]
                    maxPoint = (i, j)
                    """ actually only need to store one """
            #         endIdx = j - 1 # !!!
            else:
                continue
    print(dp)
    if maxLength == 0:
        return result
    else:
        for i in range(maxLength):
            x = int(maxPoint[0]-1)
            """   !!!!!   add list before list!!!!! \\  [string] + list \\!!!!!!! """
            result = [user1[x]] + result
            maxPoint = (maxPoint[0]-1, maxPoint[1]-1)

        """ or we can store and reverse it"""
        # while maxLen > 0:
        #     res.append(s2[endIdx])
        #     endIdx -= 1
        #     maxLen -= 1
        # return res[::-1]
    return result


user1 = ["/nine.html", "/four.html", "/six.html", "/seven.html", "/one.html"]
user2 = ["/nine.html", "/two.html", "/three.html", "/four.html", "/six.html", "/seven.html"]

print(longestCommonHistory(user1, user2))
# print(lch(user1, user2))
# ['/four.html', '/six.html', '/seven.html']





"""
longestCommonSubSequence

+ no need to consecutively 

if not a match: dp[i][j] = max(dp[i][j-1], dp[i-1][j])

start from the last position, do a while loop:
    check if left<cur and not a match: i--
    check if its a match go diagonally: i--, j-- 
    until the value is 0
    

"""
def longestCommonSubSequence(user1, user2):
    len1 = len(user1)
    len2 = len(user2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    maxLen = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if user1[i-1] == user2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(dp)

    result = []
    i, j = len1, len2
    while i >0 and j > 0 and dp[i][j]>0:
        if user1[i-1]==user2[j-1]:
            result.append(user1[i-1])
            i -= 1
            j -= 1
        elif user1[i-1]!=user2[j-1] and dp[i][j-1]<dp[i][j]:
            i -= 1
        else:
            j -= 1

    return result[::-1]


print(longestCommonSubSequence(user1, user2))
# /nine.html /four.html /six.html /seven.html

def longestCommonSubSequence2(user1, user2):
    len1 = len(user1)
    len2 = len(user2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    maxLen = 0

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if user1[i - 1] == user2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

            maxLen = max(maxLen, dp[i][j])

    index = dp[len1][len2]
    lcs = [''] * (maxLen + 1)
    lcs[-1] = '\0'

    i = len1
    j = len2
    while i > 0 and j > 0:
        if user1[i - 1] == user2[j - 1]:
            lcs[index - 1] = user1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of {} and {} is {}".format(user1, user2, ' '.join(lcs)))
    return maxLen


print(longestCommonSubSequence2(user1, user2))

def lcsubstring(S,T):

    m = len(S)
    n = len(T)

    counter = [[0]*(n+1) for x in range(m+1)]

    longest = 0
    lcs_set = []

    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = []

                    longest = c
                    """ update result by copy [i-c+1,  i+ 1]"""
                    lcs_set.append(S[i-c+1:i+1])

                elif c == longest:
                    lcs_set.append(S[i-c+1:i+1])

    return lcs_set
print(" =+++++++++")
print(lcs(user1, user2))
############################
"""
1143. Longest Common Subsequence

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
"""
"""
if not text1 or not test2: return 0
not Consecutive
abcd, ab
# # a b c d
# 0 0 0 0 0
a 0 1 1 1 1
b 0 1 2 2 2
"""

# time/space : M*N

class Solution:
    def longestCommonSubsequenceLength(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        row = len(text1) + 1
        col = len(text2) + 1

        dp = [[0] * col for _ in range(row)]
        for i in range(1, row):
            for j in range(1, col):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


# time : M*N
# space : min (M,N)

############################
"""
14. Longest Common Prefix

Input: ["flower","flow","flight"]
Output: "fl"

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        if len(strs)==1: return strs[0]
        target  = strs[0]
        prefix = ""
        for i in range(len(target)):
            for j in range(1, len(strs)):
                if len(strs[j])>i and target[i] == strs[j][i]:
                    continue
                else:
                    return prefix
            prefix += target[i]
        return prefix
