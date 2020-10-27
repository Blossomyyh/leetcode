"""
121. Best Time to Buy and Sell Stock I
buy $ sell for one time

"""
def maxProfit(self, prices) -> int:
    # mini should before maximum
    # only record maxprof & min
    pro = 0
    mini = float('inf')
    for p in prices:
        mini = min(mini, p)
        pro = max(pro, p - mini)
    return pro
"""
122. Best Time to Buy and Sell Stock II
buy any times sell any times
"""


def maxProfit(self, prices) -> int:
    p = 0
    for i in range(1, len(prices)):
        if prices[i - 1] < prices[i]:
            p += prices[i] - prices[i - 1]
    return p

"""
123. Best Time to Buy and Sell Stock III
Design an algorithm to find the maximum profit. You may complete at most two transactions.
"""
def maxProfit3(price):
    t1cost, t2cost = float('inf'), float('inf')
    t1pro, t2pro = 0,0
    for p in price:
        t1cost = min(t1cost,p)
        t1pro = max(t1pro, p-t1cost)
        # reinvest the gained profit in the second transaction
        t2cost = min(t2cost, p-t1pro)
        t2pro = max(t2pro, p-t2cost)
        print(t1cost, t1pro, t2cost, t2pro)
    return t2pro


print(maxProfit3([7,1,5,3,6,4]))
"""
t1_cost: the minimal cost of buying the stock in transaction #1. 
The minimal cost to acquire a stock would be the minimal price value 
that we have seen so far at each step.

t1_profit: the maximal profit of selling the stock in transaction #1.
 Actually, at the end of the iteration, 
 this value would be the answer for the first problem in the series, 
 i.e. Best Time to Buy and Sell Stock.

t2_cost: the minimal cost of buying the stock in transaction #2,
 while taking into account the profit gained from the previous transaction #1. 
 One can consider this as the cost of reinvestment. Similar with t1_cost, 
 we try to find the lowest price so far, 
 which in addition would be partially compensated by the profits gained from the first transaction.

t2_profit: the maximal profit of selling the stock in transaction #2. 
With the help of t2_cost as we prepared so far, we would find out the maximal profits with at most two transactions at each step

"""


"""

 dp[day_number][used_transaction_number][stock_holding_status] 
 to represent our states, 
 where stock_holding_status is a 0/1 number 
 representing whether you hold the stock or not.

The value of dp[i][j][l] represents 
the best profit we can have at the end of the i-th day,
 with j remaining transactions to make and l stocks.
"""
"""
Let dp[i][k] = maxProfit of prices[:i+1] with at most k transactions, 
the base cases and recursive relationship are

\\ (i) dp[k][i]= 0 if i <= 0 or k <= 0
\\ (ii) dp[k][i] = 
        max(
        dp[k][i-1],  \\ no transaction
        prices[i] - prices[j] + dp[k-1][j-1] for j 
        from 0 to i-1) \\ sell at i buy at j(j<i)

Because we have two choices at day i: (1) do nothing at day i, (2) maxProfit of prices[:j], buy at day j, sell at day i.

\\ Solution 1: bottom-up approach with a 2D table (Time Limit Exceeded, 208 / 211 test cases passed.)
 
 2 5 7 1 4
00 0 0 0 0
10 3 5 5 5
20
30
"""
def maxProfit(self, k, prices):

    n = len(prices)
    if n < 2:
        return 0
    dp = [[0 for _ in range(k + 1)] for _ in range(n)]
    for k1 in range(1, k + 1):
        for i in range(1, n):
            dp[i][k1] = dp[i - 1][k1]
            for j in range(i):
                tmp = prices[i] - prices[j]
                tmp += dp[j][k1 - 1] if j > 0 and k1 - 1 > 0 else 0
                dp[i][k1] = max(dp[i][k1], tmp)
    return dp[n - 1][k]