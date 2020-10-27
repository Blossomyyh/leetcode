"""
helper(left, rigth, cur):
    if length of current string == 6:
        result append string
    if left< n:
        call helper with update parameters
    le
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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