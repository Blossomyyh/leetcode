"""
836. Rectangle Overlap

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
"""

"""
\\ check whether inside can form a rectangle !!!!


"""
def isRectangleOverlap(self, rec1: [int], rec2: [int]) -> bool:
    # we can actually check if the coordinates of bottom-left and top-right can form a valid rectangle
    x1 = max(rec1[0], rec2[0])
    y1 = max(rec1[1], rec2[1])
    x2 = min(rec1[2], rec2[2])
    y2 = min(rec1[3], rec2[3])
    if x1 < x2 and y1 < y2:
        return True
    return False

def defineIntersect(rec1: [int], rec2: [int]) -> bool:
    def intersect(aleft, aright, bleft, bright):
        return max(aleft, bleft) < min(aright, bright)

    return (intersect(rec1[0], rec1[2], rec2[0], rec2[2])) and \
           (intersect(rec1[1], rec1[3], rec2[1], rec2[3]))
# check rows & cols