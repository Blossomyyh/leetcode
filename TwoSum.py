class Solution(object):
  def twoSum(self, nums, target):
    for i1, a in enumerate(nums):
      for i2, b in enumerate(nums):
        if a == b:
          continue
        if a + b == target:
          return [i1, i2]
    return []
  # N*N

  def twoSumB(self, nums, target):
    values = {}
    for i, num in enumerate(nums):
      diff = target - num
      if diff in values:
        return [i, values[diff]]
      values[num] = i
    return []
#   O(N


print(Solution().twoSumB([2, 7, 11, 15], 18))
