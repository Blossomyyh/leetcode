"""
161. One Edit Distance

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
"""
"""
find the one inside is different
    check next string 
        1. ns=nt -- check s/t[i+1:]   --- replace
        2. ns!=nt -- check s[i:]/t[i+1:] --- delete
No difference
    check length ns = nt+1 --- insert
        
"""
def isOneEditDistance(self, s: str, t: str) -> bool:
    ns = len(s)
    nt = len(t)
    # make sure ns<nt
    if ns > nt:
        ns, nt = nt, ns
        s, t = t, s

    # out - >1
    if nt - ns > 1:
        return False

    for i in range(ns):
        if s[i] != t[i]:
            if ns == nt:
                # same length - change i
                return s[i + 1:] == t[i + 1:]
            else:
                # delete ith in t
                return s[i:] == t[i + 1:]
    # no difference for s and t
    return ns + 1 == nt