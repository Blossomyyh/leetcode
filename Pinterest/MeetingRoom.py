def meeting_room(meetings, new_meeting):
    meetings.append(new_meeting)
    meetings.sort()

    for i in range(1, len(meetings)):
        if meetings[i][0] < meetings[i - 1][1]: # and meetings[i-1][0] < meetings[i][1]:
            return False

    return True

test1 = [[1300, 1500], [930, 1200], [830, 845], [840, 855]]
new1 = [1450, 1500]


print(meeting_room(test1, new1))


def meeting_room2(meetings):
    # output the available time slot
    merged = []
    meetings.sort()

    for meeting in meetings:
        if not merged or merged[-1][1] < meeting[0]:
            merged.append(meeting)
        else:
            merged[-1][1] = max(merged[-1][1], meeting[1])

    # print(merged)

    res = []
    res.append([0, merged[0][0]])
    for i in range(1, len(merged)):
        last_end = merged[i - 1][1]
        cur_start = merged[i][0]
        res.append([convert(last_end), convert(cur_start)])

    if merged[-1][1] < 2400:
        res.append([merged[-1][1], 2400])

    print(res)


def convert(time):
    res = ''
    if len(str(time)) == 3:
        res = '0' + str(time)[0] + ':' + str(time)[1:]
    elif len(str(time)) == 4:
        res = str(time)[:2] + ':' + str(time)[2:]
    return res


print(meeting_room2(test1))



###############
# 3
import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])
        print(free_rooms)
        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            print(free_rooms)
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i[1])
            print(free_rooms)
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
"""
# PUT MEETING END TIME IN HEAP --> MIN END TIME POP OUT"
heap length is length of meeting rooms
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals: return 0
        heap = []
        intervals.sort(key=lambda x: x[0])
        # only append end time
        heapq.heappush(heap, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])

        return len(heap)


"""
1229. Meeting Scheduler
"""
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
from typing import List

def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    slots1.sort(key=lambda x: x[0])
    slots2.sort(key=lambda x: x[0])
    i, j = 0, 0
    while i<len(slots1) and j< len(slots2):
        head = max(slots1[i][0], slots2[j][0])
        tail = min(slots1[i][1], slots2[j][1])
        if head + duration<=tail:
            return [head, head+duration]

        if slots1[i][1] < slots2[j][1]:
            i+= 1
        else:
            j+=1
    return []
print(minAvailableDuration(slots1, slots2, duration))
