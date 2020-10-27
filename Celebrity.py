# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# There will be exactly one celebrity
def knows(a,b):
    return True
class Solution:
    def findCelebrity(self, n: int) -> int:
        can = 0

        def secondcele(m):
            for i in range(n):
                if i == m: continue
                if knows(m, i) or not knows(i, m):
                    return False
            return True

        for i in range(1, n):
            if knows(can, i):
                can = i
        if secondcele(can):
            return can
        return -1

"""
  0 1 2
0[[1,1,0]
1,[0,1,0],
2 [1,1,1]]

0,1? --> 1,2?no, --> end, go check this candidate with all people
"""


# 2: Logical Deduction

