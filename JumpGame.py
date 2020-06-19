from typing import List
# dynamic programming
# 1.Start with the recursive backtracking solution
# 2.Optimize by using a memoization table (top-down[2] dynamic programming)
# 3.Remove the need for recursion (bottom-up dynamic programming)
# 4.Apply final tricks to reduce the time / memory complexity
#

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