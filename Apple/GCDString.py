"""
1071. Greatest Common Divisor of Strings

use gcd to count largest length
then use regex to compare
"""


import re

def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)

    def gcd(l1, l2):
        while l2:
            l1, l2 = l2, l1 % l2
        return l1

    div = gcd(len1, len2)
    pattern = "(" + str1[0:div] + ")+"
    if re.fullmatch(pattern, str1) and re.fullmatch(pattern, str2):
        return str1[0:div]
    else:
        return ''

"""
no re
"""


def gcdOfStrings(self, str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)

    # gcd
    def gcd(l1, l2):
        while l2:
            l1, l2 = l2, l1 % l2
        return l1

    div = gcd(len1, len2)
    pattern = str1[0:div]

    # valid
    def valid(pattern, string):
        l = len(pattern)
        s = 0
        while s < len(string):
            if string[s:s + l] != pattern:
                return False
            else:
                s = s + l

        return True

    if valid(pattern, str1) and valid(pattern, str2):
        return str1[0:div]
    else:
        return ''