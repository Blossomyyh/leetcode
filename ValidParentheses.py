class Solution(object):
    """
    20 Valid Parentheses
    write decent code
    use hashmap
    """
    def validParentheses(self, s):
        map = {
            '(': ')',
            '{':'}',
            '[':']'
        }
        """  for k,v in map.items() """
        reverseMap = {v:k for k,v in map.items()}
        stack = []
        for i in s:
            if i in map:
                stack.append(i)
            elif i in reverseMap:
                """!!! not pop --> use stack[-1]!!!!!  && check the length before -1!!!!"""
                if len(stack) == 0 or stack[-1] != reverseMap[i]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0

print(Solution().validParentheses('(){([])}'))
# True

print(Solution().validParentheses('(){(['))
# False