"""
 5. longestPalindromeSubstring


expand around centers:
for each ele in string:
    expand (i,i)
    expand (i, i+1)
    record the max length returned by expansion

expand func(start, end):
    if start-1>=0 and end + 1< len and start == end:
        expand(start-1, end +1)
    return largest length of the palindrome (end-start+1)

"""
test  = "aba"
test = "a"
test = "ssdbbdss"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s)==0:
            return ""
        if len(s)==1:
            return s

        def expand(start, end):
            # do iteration
            """use while loop """
            while start>=0 and end<len(s) and s[start]==s[end]:
                start -= 1
                end += 1
            return end-start-1

        res = ""
        # i= 1
        for i in range(len(s)):
            # i is center, expand
            p1 = expand(i, i)
            # interval/gap after i is center , expand
            p2 = expand(i, i+1)
            if p1>len(res):
                res = s[i-p1//2: i+p1//2+1]
            if p2>len(res):
                res = s[i-p2//2+1: i+p2//2+1]
        return res
print(Solution().longestPalindrome(test))












