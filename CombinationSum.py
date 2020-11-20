"""
Combination Sum

Time : O(N^(T/M))
T: target sum
M: minimum value
DFS in a n-ary tree --> T/M + 1 will be the deepest depth in the tree
Space: O(T/M)

"""
candidates = [10,1,2,7,6,1,5]
def combinationSum2(candidates, target: int):
    candidates.sort()
    res = []

    def dfs(cursum, cur, index):
        if cursum == target:
            res.append(cur)
            return
        for i in range(index, len(candidates)):
            if cursum + candidates[i] > target:
                return
            else:
                """not allow duplication --> if== then continue"""
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                dfs(cursum + candidates[i], cur + [candidates[i]], i+1)

    dfs(0, [], 0)
    return res

print(combinationSum2(candidates, 8))


def combinationSum(self, candidates, target: int) :
    candidates.sort()
    res = []

    def combination(cur, cursum, idx):
        if cursum == target:
            res.append(cur)
            return
        for i in range(idx, len(candidates)):
            if cursum + candidates[i] > target: break
            """ if we can allow dup for a ele --> dfs starting from i itself!!"""
            combination(cur + [candidates[i]], cursum + candidates[i], i)

    combination([], 0, 0)
    return res

#jsdlkf
"""
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
"""

""" \\ avoid dup --> start should update to i next"""
def combinationSum3(self, k: int, n: int):
    res = []

    def helper(curlen, cursum, curlist, start):

        if curlen == k and cursum == n:
            res.append(curlist)
            return
        for i in range(start, 10):
            if cursum + i <= n:
                helper(curlen + 1, cursum + i, curlist + [i], i + 1)

        return

    helper(0, 0, [], 1)
    return list(res)


"""
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
"""

"""
\\ dp solution
one line
target iterate first
second is numbers
since allow 211 and 112
[1, 0,0,0,0]

dp[j] += dp[j - nums[i - 1]] 
"""
def combinationSum4(self, nums, target: int) -> int:
    if not nums:
        if target == 0:
            return 1
        return 0
    if len(nums) == 1 and target % nums[0] == 0:
        return 1
    dp = [0] * (target + 1)

    for j in range(target + 1):
        if j == 0:
            dp[j] = 1
            continue
        for i in range(1, len(nums) + 1):
            if j - nums[i - 1] >= 0:
                dp[j] += dp[j - nums[i - 1]]
    return dp[-1]