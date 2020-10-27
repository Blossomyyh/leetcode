"""
for day in set:
    dp[i] = Min(dp[i-1]+count(1),
            dp[i-7]+count(7),
            dp[i-30]+count(30))

        if i-dur<0 --> then use dp[0]
not set:
    cost = dp[i-1]
"""


class Solution:
    def mincostTickets(self, days, costs) -> int:
        dp = [float('inf')] * 366
        dp[0] = 0

        for i in range(1, days[-1] + 1):
            if i > 365:
                return 0
            if i in days:
                for cost, duration in zip(costs, [1, 7, 30]):

                    if i - duration >= 0:

                        dp[i] = min(dp[i], dp[i - duration] + cost)
                    else:
                        dp[i] = min(dp[i], dp[0] + cost)

            else:
                dp[i] = dp[i - 1]

        return dp[days[-1]]