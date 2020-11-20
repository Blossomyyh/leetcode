# Combinations:
"""
time O(k C^k_N)
    length * number of combination
space O(C^k_N)
"""

from typing import List
def combine(self, n, k):
    res = []
    self.dfs(range(1, n + 1), k, 0, [], res)
    return res


def dfs(self, nums, k, index, path, res):
    # if k < 0:  #backtracking
    # return
    if k == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(nums)):
        self.dfs(nums, k - 1, i + 1, path + [nums[i]], res)

#
# Permutations
# I


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            # return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)


"""
sol 2 
use exchange to permutate
1. has to first res = []
2. res += b()
3. if == len, return [nums[:]]  \\ X - no [res] !!!!!
 \\ means return a copy of this rather than nums itself
\\ or it may have shallow copy and all change to the same 
"""
def permutation(nums):
    def backtracking(start, res):
        if start == len(res)-1:
            print(res)

            return [res[:]]
        result = []
        for i in range(start, len(res)):
            res[start], res[i] = res[i], res[start]
            # print(res)
            result += backtracking(start + 1, res)
            res[start], res[i] = res[i], res[start]
            # print(res)
        return result

    return backtracking(0, nums)
print(permutation([1,2,3]))

"""
sol 3 -- just use a visited to get all visited 
construct the path along the way
"""
class solution:
    def dfs(self, nums, path, start):
        if len(path) == len(nums):
            self.res.append(path[:])
            return
        for i in range(len(nums)):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(nums, path + [nums[i]], i+1)
                self.visited[i] = False

    def permutation3(self, nums):
        self.res = []
        self.visited = [False]*len(nums)
        nums.sort()
        self.dfs(nums, [], 0)

#
# Permutations
# II
#

def permuteUnique(self, nums):
    res, visited = [], [False] * len(nums)
    nums.sort()
    self.dfs(nums, visited, [], res)
    return res


def dfs(self, nums, visited, path, res):
    if len(nums) == len(path):
        res.append(path)
        return
    for i in range(len(nums)):
        if not visited[i]:
            # except  i == 0
            # except 2 number are identical and the one before hasn't been marked
            # we have already go through this one, no need to go another same one again
            # so just pass this case
            if i > 0 and not visited[i - 1] and nums[i] == nums[i - 1]:  # here should pay attention
                continue
            visited[i] = True
            self.dfs(nums, visited, path + [nums[i]], res)
            visited[i] = False


"""
sol2 for unique permutation
"""
def permutation(nums):
    def backtracking(start, res):
        if start == len(res)-1:
            print(res)

            return [res[:]]
        result = []
        for i in range(start, len(res)):
            """ 
            just need to make sure i>start and has same previously --> skip this case
            """
            if i>start and nums[i-1]==nums[i]:
                continue
            res[start], res[i] = res[i], res[start]
            # print(res)
            result += backtracking(start + 1, res)
            res[start], res[i] = res[i], res[start]
            # print(res)
        return result

    return backtracking(0, nums)
print(permutation([1,2,2]))
# Subsets
# 1


def subsets1(self, nums):
    res = []
    self.dfs(sorted(nums), 0, [], res)
    return res


def dfs(self, nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        self.dfs(nums, i + 1, path + [nums[i]], res)


# Subsets
# II

nums = [1,2,2,2]
class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res


    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            """
            this time --> we allow 1,2,2
            so we make i > start-index rather than i>0and not visited
            """
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)

print(Solution().subsetsWithDup(nums))
# Combination
# Sum


def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return
    for i in range(index, len(nums)):
        self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


# Combination
# Sum
# II


def combinationSum2(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res


def dfs(self, candidates, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(candidates)):
        if i > index and candidates[i] == candidates[i - 1]:
            continue
        self.dfs(candidates, target - candidates[i], i + 1, path + [candidates[i]], res)