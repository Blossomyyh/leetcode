"""
Atoi

1. strip()
2. get first characters +/-
3. add numbers until not digits

"""

class Solution:
    def myAtoi(self, str: str) -> int:

        lists = list(str.strip())
        if len(lists) == 0:
            return 0
        sign = -1 if lists[0] == '-' else 1
        if lists[0] in ['-', '+']:
            del lists[0]
        res = 0
        i = 0
        while i < len(lists) and lists[i].isdigit():
            res = res * 10 + ord(lists[i]) - ord('0')

            i += 1
        return max(-2 ** 31, min(sign * res, 2 ** 31 - 1))


