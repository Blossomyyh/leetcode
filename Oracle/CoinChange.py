"""
518. Coin Change 2 ---- Knapsack series


Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

"""

class Solution:
    def change(self, amount: int, coins) -> int:
        if not coins:
            if amount == 0:
                return 1
            return 0
        if len(coins) == 1 and amount % coins[0] == 0:
            return 1
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            for j in range(amount + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 0
                    continue
                elif i == 0:
                    dp[i][j] = 0
                    continue
                elif j == 0:
                    dp[i][j] = 1
                    continue
                else:
                    dp[i][j] += dp[i - 1][j]
                    if j - coins[i - 1] >= 0:
                        dp[i][j] += dp[i][j - coins[i - 1]]
                        # print(dp)
        return dp[-1][-1]
    


"""
with one line dp

coin should not have 211 and 112 both acceptable
nums first
target second
"""


def combinationSum4(self, nums, target: int) -> int:
    if not nums:
        if target == 0:
            return 1
        return 0
    if len(nums) == 1 and target % nums[0] == 0:
        return 1
    dp = [0] * (target + 1)

    for i in range(len(nums) + 1):
        for j in range(target + 1):
            if j == 0:
                dp[j] = 1
                continue
            else:
                if j - nums[i - 1] >= 0:
                    dp[j] += dp[j - nums[i - 1]]
                print(dp[j])

            print(dp)

    return dp[-1]