"""
Problem Statement
In our service, processes sometimes get into an unhealthy state.
One of the symptoms is that the CPU load remains high for a long period.
But CPU load tends to be spikey. We have decided to try an approach
where we continuously average the CPU load over a 5 minute period to smooth out the CPU load and
then use that to decide if processes are unhealthy.
Please create a class that can listen to a series of CPU values and,
on demand, output the average of the last 5 minute’s worth of data.

Supports a record(value) call which records the value and the time
at which the API call was issued.
You can assume value is greater than zero;
and the required precision is seconds.

Supports an average() call which returns the average of values recorded for the previous 5 minutes.
If there are no recorded values in the previous 5 minutes then -1 will be returned.

Example
At 23:00:17: record(10) is called
At 23:00:25: record(15) is called
At 23:04:10: record(10) is called
At 23:05:15: record(20) is called
At 23:05:16: average() is called, and returns 13.75
At 23:06:32: record(41) is called
At 23:07:43: average() is called, and returns 23.66
At 23:41:50: average() is called, and return -1

list record 5 min - 5*60 - 300
key - curtime ; value - record
key -> 230017 -> 17,
5:17
start = 23:00:17

Edge case:
1. required minutes < 0 -> raise error
2. no record --> -1
3. hours > 1 --> delete odd one
4. input -> valid
5. existing key -> raise error
6. ordereddict
"""
from collections import defaultdict
import time


class CPU:
    def __init__(self, minutes):
        self.load5 = defaultdict(int)
        self.minutes = minutes

    def _shrinkMemory(self, curtime):
        prevtime = curtime - 60 * self.minutes
        print(prevtime)
        # traversal keys and find time<cur-5min
        for time in self.load5.keys():
            if time < prevtime:
                del self.load5[time]

    def record(self, num):
        # delete record with time < 5min
        curtime = time.time()
        print(curtime)
        self._shrinkMemory(curtime)
        # add record
        if curtime in self.load5:
            return
        self.load5[curtime] = num

    def average(self):
        # delete record with time < 5min
        curtime = time.time()
        print(curtime)
        self._shrinkMemory(curtime)
        # return -1 if no record available
        if len(self.load5) == 0:
            print("Average record: -1")
            return -1
        else:
            # return average of records available
            avgRecord = sum(self.load5.values()) / len(self.load5)
            print("Average record: " + str(avgRecord))
            return avgRecord


cpu = CPU(5)
# cpu.record(10)
# cpu.record(15)
# cpu.record(10)
# cpu.record(20)
cpu.average()
