"""
# Definition for an Interval.
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

"""
\\ 1. sort 
"""
class Solution(object):
    # def employeeFreeTime(self, schedule):
    #     ints = sorted([i for s in schedule for i in s], key=lambda x: x.start)
    #     res, pre = [], ints[0]
    #     for i in ints[1:]:
    #         if i.start <= pre.end and i.end > pre.end:
    #             pre.end = i.end
    #         elif i.start > pre.end:
    #             res.append(Interval(pre.end, i.start))
    #             pre = i
    #     return res
    def employeeFreeTime(self, schedule: [[Interval]]):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """
        work = []
        for employ in schedule:
            for time in employ:
                # print(time, time.start, time.end)
                work.append([time.start, time.end])

        work.sort(key=lambda x: x[0])
        # print(work)
        merge = []
        for curitem in work:
            if not merge:
                merge.append(curitem)
            else:
                prev = merge[-1]
                # print(curitem, prev)
                if prev[1] >= curitem[0] and prev[1] < curitem[1]:
                    prev[1] = curitem[1]
                elif prev[1] < curitem[0]:
                    merge.append(curitem)

        result = []
        p = None
        for m in merge:
            if not p:
                p = m
                continue
            else:
                result.append(Interval(p[1], m[0]))
                print(p[1], m[0])
                p = m
        return result

print(Solution().employeeFreeTime([[Interval(1,3),Interval(6,7)],[Interval(2,4)],[Interval(2,5),Interval(9,12)]]))
# [[5,6],[7,9]]
"""
\\ 2. priority queue
"""
import heapq
class solutionn:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: [[Interval]]
        :rtype: [Interval]
        """

        heap = []
        for i in schedule:
            for m in i:
                heapq.heappush(heap, [m.start, m.end])
        res = []
        s, e = heapq.heappop(heap)
        while heap:
            n = heapq.heappop(heap)
            if n[1] <= e:
                continue
            elif n[0] <= e and n[1] > e:
                # update e
                e = n[1]
            elif n[0] > e:
                res.append(Interval(e, n[0]))
                s = n[0]
                e = n[1]
        return res
