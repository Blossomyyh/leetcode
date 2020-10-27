"""
729. My Calendar I


Balanced Tree

\\ Treemap --> java
We need a data structure that keeps elements sorted and supports fast insertion.
In Java, a TreeMap is the perfect candidate. In Python, we can build our own binary tree structure.

TreeMap where the keys are the start of each interval,
and the values are the ends of those intervals.
 When inserting the interval [start, end),
 we check if there is a conflict on each side with neighboring intervals:
"""

"""
[1,2]
   [2,3]
[0,1]   [4,5]
"""
class Node:
    def __init__(self,s,e ):
        self.s = s
        self.e = e
        self.left = None
        self.right = None

import bisect

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book_helper(self, s, e, node):
        if s >= node.e:
            if node.right:
                return self.book_helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif e <= node.s:
            if node.left:
                return self.book_helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else:
            return False

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.book_helper(start, end, self.root)



########################
    """
    \\ sol binary search --- bisect
    """


"""
use queue to store all start & end
get insert idx with bisect
compare the same? idx%2==1 --> false
insert all!!!!
 \\ time is [start,end) so insert [start, \\end-1]
"""

from collections import deque

import bisect
class MyCalendar(object):

    def __init__(self):
        self.booked_times = deque()

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        --    -----
         --- -  -
         --------
        """

        start_index = bisect.bisect_left(self.booked_times, start)
        end_index = bisect.bisect_left(self.booked_times, end)
        print(start_index, end_index)
        if start_index != end_index or start_index % 2:
            return False


        self.booked_times.insert(start_index, end - 1)
        self.booked_times.insert(start_index, start)
        return True

"""list version"""
import bisect
class MyCalendar(object):
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        --    -----
         --- -  -
         --------
        """
        idxs = bisect.bisect_left(self.intervals, start)
        idxe = bisect.bisect_left(self.intervals, end)

        if idxs != idxe or idxs % 2 == 1:
            return False
        # cost O(N) to insert
        self.intervals = self.intervals[:idxs] + [start, end - 1] + self.intervals[idxs:]

        return True
"""
Implement a MyCalendarTwo class to store your events. 
A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). 
Formally, this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.


"""

class MyCalendarTwo:

    def __init__(self):
        # record all events
        self.time = []
        # overloap only record time with 2 events
        self.overlap = []

    def book(self, start: int, end: int) -> bool:
        # FIRST check whether intersect with overlap - yes-> False
        for i,j in self.overlap:
            if start<j and end>i:
                return False
        # not insec with overlap check insec with time -> yes-> put min to overlap
        for i, j in self.time:
            if start<j and i<end:
                self.overlap.append((max(start, i), min(end, j)))
        self.time.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)



"""
When booking a new event [start, end), count delta[start]++ and delta[end]--.
When processing the values of delta in sorted order of their keys, 
the largest such value is the answer.

In Python, we sort the set each time instead, 
"""
from collections import Counter


class MyCalendarThree:
    def __init__(self):
        self.delta = Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        active = ans = 0

        sortc = sorted(self.delta)
        # print(self.delta)
        # print(sortc)
        for i in sortc:
            active += self.delta[i]
            if active > ans: ans = active

        return ans



        # Your MyCalendarThree object will be instantiated and called as such:
        # obj = MyCalendarThree()
        # param_1 = obj.book(start,end)
        # MyCalendarThree();
        # MyCalendarThree.book(10, 20); // returns 1
        # MyCalendarThree.book(50, 60); // returns 1
        # MyCalendarThree.book(10, 40); // returns 2
        # MyCalendarThree.book(5, 15); // returns 3
        # MyCalendarThree.book(5, 10); // returns 3
        # MyCalendarThree.book(25, 55); // returns 3
        # Explanation:
        # The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
        # The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
        # The remaining events cause the maximum K-booking to be only a 3-booking.
        # Note that the last event locally causes a 2-booking, but the answer is still 3 because
        # eg. [10, 20), [10, 40), and [5, 15) are still triple booked.