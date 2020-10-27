"""

helper(left, rigth, cur):
    if length of current string == 6:
        result append string
    if left< n:
        call helper with update parameters
    le
"""
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n == 0: return []

        def helper(left, right, cur):
            if len(cur) == n * 2:
                result.append(cur)
                return
            if left < n:
                helper(left + 1, right, cur + '(')
            if right < n and left > right:
                helper(left, right + 1, cur + ')')

        helper(0, 0, "")
        return result

    def whilegenerate(self, n):
        result = []
        stack = [(0, 0, "")]
        while stack:
            left, right, cur = stack.pop()
            if len(cur) == n * 2:
                result.append(cur)
                continue
            if left < n:
                stack.append((left + 1, right, cur + '('))
            if right < n and left > right:
                stack.append((left, right + 1, cur + ')'))

        return result




'''
+dynamic programming

It is also possible to solve the problem explicitly using dynamic programming. Define f(n) as the set of all valid parentheses when there are n opening parentheses. Then symbolically, f(n+1) follows below recursive equation,
f(n+1) = (f(0))f(n) + (f(1))f(n-1) + ... + (f(n-1))f(1) + (f(n))f(0)
((f(i))f(j) means that the valid parentheses of f(i) added by a pair of parentheses outside concatenated with the valid parentheses of f(j), i.e. this is a loop.)


'''

#
# Generate one pair: ()
#
# Generate 0 pair inside, n - 1 afterward: () (...)...
#
# Generate 1 pair inside, n - 2 afterward: (()) (...)...
#
# ...
#
# Generate n - 1 pair inside, 0 afterward: ((...))
#
# I bet you see the overlapping subproblems here. Here is the code:
#
# (you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, and we are taking into account all possible of combinations of them)

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]