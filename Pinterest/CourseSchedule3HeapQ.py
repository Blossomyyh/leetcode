"""

630. Course Schedule III
sort coursed based on end time
choose 1 push into maxheap if endtime< endi and
if not pop one with max time replace if meet ddl
"""
import heapq as hq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        if not courses: return 0
        if len(courses) == 1: return 1
        courses = sorted(courses, key=lambda x: x[1])
        courses_taken = []
        duration = 0
        for start, end in courses:
            if duration + start <= end:
                hq.heappush(courses_taken, -start)
                duration += start
            elif courses_taken and start < abs(courses_taken[0]):
                max_duration = hq.heappop(courses_taken)
                hq.heappush(courses_taken, -start)
                duration += start + max_duration

        return len(courses_taken)