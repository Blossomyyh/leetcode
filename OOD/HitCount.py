"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.
"""
# Optimized and Scalable Solution

# compare with dictionary: dic may have endless list & need to sort the time
# The third solution creates an array of 300 elements. Every element of the array comprises of [frequency, timestamp].
# Timestamp 1 maps to index 0. Timestamp 100 maps to index 99.
# Use modulo mathematics to update it. hit: O(1). get_hit: O(300). This solution will scale perfectly!

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time = [[0,t+1] for t in range(300)]

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        # ts = 301 means (301-1)%300
        i = (timestamp-1)%300
        if self.time[i][1]== timestamp:
            self.time[i][0]+=1
        else:
            self.time[i]=[1, timestamp]

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        res = 0
        for i in range(300):
            """compare whether in range timestamp-self.time[i][1]"""
            if timestamp-self.time[i][1]<300:
                res += self.time[i][0]
        return res


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# HitCounter counter = new HitCounter();
#
#  hit at timestamp 1.
# counter.hit(1);
#
# // hit at timestamp 2.
# counter.hit(2);
#
# // hit at timestamp 3.
# counter.hit(3);
#
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
#
# // hit at timestamp 300.
# counter.hit(300);
# 
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
#
# // get hits at timestamp 301, should return 3.
# counter.getHits(301);