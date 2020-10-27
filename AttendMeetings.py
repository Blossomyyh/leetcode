"""
252. Meeting Rooms

 def overlap(self, a, b):
        return a[0] <= b[1] and b[0] <= a[1]

"""



def canAttendMeetings(self, intervals) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i - 1][0] < intervals[i][1] and intervals[i][0] < intervals[i - 1][1]:
            return False
    return True