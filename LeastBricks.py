"""
554. Brick Wall
Hashmap solution:
store all intervals with frequency

"""

def leastBricks(self, wall) -> int:
    '''
    store all intervals with frequency
    '''
    dic = {}
    size = len(wall)
    res = size
    for wallist in wall:
        s = 0
        for i in range(len(wallist) - 1):
            item = wallist[i]
            dic[s + item] = dic.get(s + item, 0) + 1
            if size - dic[s + item] < res:
                res = size - dic[s + item]
            s += item
            # print(dic, res)
    return res

'''
Time complexity : O(n). We traverse over the complete bricks only once.
 nn is the total number of bricks in a wall.

Space complexity : O(m). 
mapmap will contain atmost mm entries, 
where mm refers to the width of the wall.
'''