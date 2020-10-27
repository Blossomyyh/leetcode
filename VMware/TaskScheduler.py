"""
621. Task Scheduler
# asynchronous processing
"""
## RC ##
## APPROACH : HASHMAP ##
## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1

## Ex: {A:6,B:4,C:2} n = 2
## final o/p will be
## slot size / cycle size = 3
## Number of rows = number of A's (most freq element)
# [
#     [A, B,      C],
#     [A, B,      C],
#     [A, B,      idle],
#     [A, B,      idle],
#     [A, idle,   idle],
#     [A   -        - ],
# ]
#
# so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
# ans   =     rows_except_last   * columns +        last_row


## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)


## TIME COMPLEXITY : O(N) ##
## SPACE COMPLEXITY : O(1) ##


"""
A-3, B-3, C-3, D-3
ABCDABCDABCD with n = 2!
only need to calculate last BCD
"""

from collections import Counter
def leastInterval(self, tasks:[str], n: int) -> int:
    count = Counter(tasks)
    maxnum = max(count.values())
    if n ==0:
        return len(tasks)
    intervals = (n+1)*(maxnum-1)
    freq = list(count.values())
    addtional = 0
    for i in freq:
        if i == maxnum:
            addtional +=1
    ans = intervals + addtional
    return max(ans, len(tasks))
