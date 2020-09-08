"""


My idea is simple, it is kind of DP or linear search or whatever ...

One observation is that the answer should reach the end of string s.
Otherwise, you can always extend the hypothetical answer to the end of string s
which will be lexicographically larger than the hypothetical answer.

Next, let's assume the current dp answer is stored in a variable pre.
The idea is that when moving one letter backward,
pre either stays the same or it would be the current index.
And when we compare current index substring against pre substring,
we only need to compare upto index pre,
because we already know the comparison results beyond pre,
and we know it will be lexicographically smaller
(because pre is the currently lexicographically largest substring index).
The runtime complexity will be O(n), since we compare each letter once in the worst case.
 Space complexity is apprarently O(1)

Note that I have put a naive string comparison in comment section
which will be much slower (should be O(n^2) runtime),
so replacing it with the comparison upto pre gives much faster runtime.
"""















class Solution:
    def lastSubstring(self, s: str) -> str:
        i ,j , k =0 ,1 ,0
        n=len(s)
        while j+k<n:

            if s[i+k]==s[j + k] :
                k+=1
                continue
            elif s[i+k]>s[j+ k ]:
                j=j+k+1
            else:
                i=max(j,i + k+1)
                j=i+1
            k=0
        return s[i:]