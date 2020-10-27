
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


"""


def isValid(self, s: str) -> bool:

    stack = []
    mapping = {')':'(', ']': '[', '}': '{'}
    for ch in s:
        if ch in mapping:
            if not stack or mapping[ch]!=stack[-1]:
                return False
            else:
                stack.pop()
        else:
            stack.append(ch)
    return not stack
