"""
435. Non-overlapping Intervals
Given a collection of intervals,
find the minimum number of intervals you need to remove
 to make the rest of the intervals non-overlapping.

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
"""

"""
greedy solution
Sorting takes O(nlog(n)) time.
 O(1).
\\ simple update with currend time
"""


def eraseOverlapIntervals(self, intervals: [[int]]) -> int:
    if not intervals: return 0
    intervals.sort(key=lambda x: x[0])
    currend, count = intervals[0][1], 0
    # count -- delete one
    for x in intervals[1:]:
        if x[0] < currend:
            # overlapped
            count += 1
            # get min end
            currend = min(currend, x[1])
        else:
            # nonoverlapped -- update end
            currend = x[1]
    return count

"""
Dynamic programming
\\ tricky --- min to delete ==== MAX to maintain
dp[i] == max intervals we can have 

O(n^2) O(n)
"""
def eraseOverlapIntervals(self, intervals:[[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort()  # sort by start time
    dp = [0] * len(intervals)
    dp[0] = 1
    for i in range(1, len(intervals)):
        for j in range(i - 1, -1, -1):
            """ start from i - 1"""
            # intervals i and j overlap?
            # --- ---
            #   ----
            if intervals[j][1] > intervals[i][0]:
                # overlap
                dp[i] = max(dp[j], dp[i])
            else:
                # overlap
                dp[i] = max(dp[j] + 1, dp[i])
                break
    # print(dp)
    """ cal the delete one"""
    return len(intervals) - dp[-1]
