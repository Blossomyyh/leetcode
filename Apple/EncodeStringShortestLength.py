"""
471. Encode String with Shortest Length

Given a non-empty string, encode the string such that its encoded length is the shortest.
The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
"""
"""
\\ Dynamic Programming
Memorization: 
    just use substring as key of memoization. strEncoding[str] = shortest encoding of str.

\\ 1. base case - selfrepeating
    repeatingIdx = 
        \\ (s + s).find(s, 1), 
        \\ repeatingIdx < len(s).
        !!! find another s[:a] in s --> s[:a] is repeating

\\ 2. Recursion by Iterating string splitting point:
E.g., 'abbbabbbc' -> strEncoding(abbbabbb) + strEncoding(c)

**  time for .find()
    It is O(n) with KMP algorithm for string matching.

DP 
"""
class Solution(object):
    """
    dp[i][j] is the encode of substring including index i to index j.

    dp[i][j] =
        min(dp[i][j], dp[i][k]+dp[k][j], potential_cand) in terms of length.

    dp[i][j] = s[i:j+1] originally

    potentail_cand = 'n'+'[' + encode(pattern) + ']',
        where pattern is some repeating string in the original substring and n is the number of repeating times.
    """
    def encodeDP(self, s: str) -> str:
        """
        k > 0
        If an encoding process does not make the string shorter,
        then do not encode it. If there are several solutions, return any of them.
        """
        n = len(s)
        dp = [[''] * n  for _ in range(n)]

        for j in range(n):
            for i in range(j, -1, -1):
                """1. get original substring"""
                sub = s[i:j+1]
                dp[i][j] = sub
                """2. len>4 then go find substrings replace this sub"""
                if j-i>=4:
                    """check dp[i][k]+dp[k+1][j] < cur? - replace"""
                    for k in range(i,j):
                        if len(dp[i][k] +dp[k+1][j]) <len(dp[i][j]):
                            dp[i][j] = dp[i][k] + dp[k + 1][j]

                    """check cur has repeated -> replace"""
                    idxrepeat = (sub+sub).find(sub, 1)

                    candidate = str((j-i+1)//idxrepeat) + '['+dp[i][i+idxrepeat-1]+']'
                    if len(candidate)<len(dp[i][j]):
                        dp[i][j] = candidate
        for i in dp:
            print(i)
        return dp[0][n-1]

Solution().encodeDP("aaaababab")

"""
['a', 'aa', 'aaa', 'aaaa', 'aaaab', 'aaaaba', 'aaaabab', 'aaaababa', 'aaa3[ab]']
['', 'a', 'aa', 'aaa', 'aaab', 'aaaba', 'aaabab', 'aaababa', 'aa3[ab]']
['', '', 'a', 'aa', 'aab', 'aaba', 'aabab', 'aababa', 'a3[ab]']
['', '', '', 'a', 'ab', 'aba', 'abab', 'ababa', '3[ab]']
['', '', '', '', 'b', 'ba', 'bab', 'baba', 'babab']
['', '', '', '', '', 'a', 'ab', 'aba', 'abab']
['', '', '', '', '', '', 'b', 'ba', 'bab']
['', '', '', '', '', '', '', 'a', 'ab']
['', '', '', '', '', '', '', '', 'b']
"""

"""
\\ (s+s).find(s,1) < s.size() \\  is equivalent to substring repetition?

Proof: 
    Let N = s.size() and L := (s+s).find(s,1), 
    actually we can prove that the following 2 statements are equivalent:

    1. 0 < L < N;
    2.N%L == 0 and s[i] == s[i%L] is true for any i in [0, N). 
    (which means s.substr(0,L) is the repetitive substring)
    
    Consider function char f(int i) { return s[i%N]; }, obviously it has a period N.

    \\ "1 => 2": From condition 1, we have for any i in [0,N)
    
        s[i] == (s+s)[i+L] == s[(i+L)%N],

    which means L is also a positive period of function f. Note that N == L*(N/L)+N%L, so we have
    f(i) == f(i+N) == f(i+L*(N/L)+N%L) == f(i+N%L),
    which means N%L is also a period of f. 
    
    Note that N%L < L but L := (s+s).
    find(s,1) is the minimum positive period of function f,
     so we must have N%L == 0. Note that i == L*(i/L)+i%L, so we have
    s[i] == f(i) == f(L*(i/L)+i%L) == f(i%L) == s[i%L],
    so condition 2 is obtained.
    
    
    \\ "2=>1": If condition 2 holds, for any i in [0,N), note that N%L == 0, we have

    (s+s)[i+L] == s[(i+L)%N] == s[((i+L)%N)%L] == s[(i+L)%L] == s[i],
    which means (s+s).substr(L,N) == s, so condition 1 is obtained.
"""