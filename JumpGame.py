from typing import List
# dynamic programming
# 1.Start with the recursive backtracking solution
# 2.Optimize by using a memoization table (top-down[2] dynamic programming)
# 3.Remove the need for recursion (bottom-up dynamic programming)
# 4.Apply final tricks to reduce the time / memory complexity
#



'''
\\ dp

if maxpos < current index 
    false
else
    update maxpos with nums[i]+i

true
'''
class Solution:
    def canJump(self, nums: List[int]):
        if len(nums) == 1: return True
        maxpos = 0
        for idx, i in enumerate(nums):
            if maxpos < idx:
                return False
            maxpos = max(maxpos, nums[idx] + idx)

        return True


"""backtraching"""

# Time complexity : O(2^n)
# 2^n2 (upper bound) ways of jumping from the first position to the last, where nn is the length of array nums.
#https://leetcode.com/problems/jump-game/solution/

# Space complexity : O(n)O(n). Recursion requires additional memory for the stack frames.


class Solution:
    def jump(self, nums: List[int], m: int):
        if m == len(nums) - 1:
            return True
        """keypoint: min(len(nums) - 1, m + nums[m])"""
        further = min(len(nums) - 1, m + nums[m])
        """range between start and !!!!!! end-1 !!!!!!"""
        for n in range(further,m,-1):
            if self.jump(nums, n):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.jump(nums, 0)




# canJump([2,3,1,1,4])
"""
45. Jump Game II
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
    
\\ when curpos < curindex ---> we should jump to maxpos
        update jump and maxpos
    
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        jump = 1
        curpos = nums[0]
        maxpos = nums[0]
        for i in range(1, len(nums)):
            if maxpos < i:
                return 0
            if curpos < i:
                curpos = maxpos
                jump += 1
            maxpos = max(maxpos, nums[i] + i)

        return jump


"""
1306. Jump Game III

\\ iteration backtracking
when visited a node with 2 directions, no need to backtracking
mark it as \\ negative!!
"""
from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        while queue:
            idx = queue.popleft()
            if arr[idx]==0:
                return True
            if arr[idx]<0:
                continue
            if 0<=idx+ arr[idx]<len(arr):
                queue.append(idx+ arr[idx])
            if 0<=idx- arr[idx]<len(arr):
                queue.append(idx- arr[idx])
            arr[idx] = -arr[idx]
        return False

def canReach(self, arr: List[int], start: int) -> bool:
    if 0 <= start < len(arr) and arr[start] >= 0:
        if arr[start] == 0:
            return True
        arr[start] = -arr[start]
        return self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])

    return False