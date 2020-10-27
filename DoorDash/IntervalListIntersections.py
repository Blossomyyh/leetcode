"""
986. Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.
 represented as a closed interval.

 TWO POINTERS
 i, j compare with end and start

SITUATION --- overlap
   ----    ----
----         ------

----    ----           ----
----        ----    ---

"""

def intervalIntersection(self, A, B):

    # start with A first B second
    i = 0
    j = 0
    res = []
    while i < len(A) and j < len(B):
        if A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
            # Criss-cross lock
            s = max(A[i][0], B[j][0])
            e = min(A[i][1], B[j][1])
            res.append([s, e])
        if A[i][1] <= B[j][1]:
            i += 1
        else:
            j += 1
    return res


