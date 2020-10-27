"""
---
 ---
 --
    --
"""


class Solution:
    def insert(self, intervals, newInterval) :
        res = []
        idx = 0
        start, end = newInterval[0], newInterval[1]
        while idx < len(intervals) and intervals[idx][0] <= start:
            res.append(intervals[idx])
            idx += 1
        if not res or res[-1][1] < start:
            res.append(newInterval)
        elif res[-1][1] >= start and res[-1][1] < end:
            res[-1][1] = end
        print(res)
        while idx < len(intervals):
            interval = intervals[idx]
            idx += 1
            if res[-1][1] >= interval[0] and res[-1][1] < interval[1]:
                res[-1][1] = interval[1]
                continue
            if res[-1][1] < interval[0]:
                res.append(interval)
        return res




"""
1272. Remove Interval
  ------ 
 --- - ----
 ----------
 [[0,5]]
[2,3]
out:[[0,2],[3,5]]
"""


class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        res = []
        for i in intervals:
            if i[0] < toBeRemoved[0] and i[1] > toBeRemoved[0] and i[1] <= toBeRemoved[1]:
                i[1] = toBeRemoved[0]
            elif i[0] >= toBeRemoved[0] and i[1] <= toBeRemoved[1]:
                continue
            elif toBeRemoved[0] <= i[0] < toBeRemoved[1] and i[1] > toBeRemoved[0]:
                i[0] = toBeRemoved[1]
            elif i[0] < toBeRemoved[0] and i[1] > toBeRemoved[1]:
                res.append([i[0], toBeRemoved[0]])
                i[0] = toBeRemoved[1]

            res.append(i)
        return res