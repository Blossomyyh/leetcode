"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.
"""
class Solution:
    """
    enumerate ->

    keep a count of iterations.
    adds a counter to an iterable and returns it in a form of enumerate object.
    This enumerate object can then be used directly in
    for loops or be converted into a list of tuples using list() method.

    [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for ix, ch in enumerate(s):
            if ch not in d:
                if t[ix] in d.values():
                    return False
                d[ch] = t[ix]
            else:
                if d[ch] != t[ix]:
                    return False
        return True


    def isIsomorphic2(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False
        return True