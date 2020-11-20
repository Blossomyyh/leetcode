"""
486.Predict the Winner

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False
"""



def PredictTheWinnerRec(self, nums: [int]) -> bool:
    return winner(nums, 0, len(nums)-1, 1) >= 0

# start + end + turn 1/-1
# make player 1 -> *1 get max
# make player 2 -> *-1 get min
def winner(nums, s, e, turn):
    if s== e:
        return turn * nums[s]
    choosefront = turn * nums[s] + winner(nums, s+1, e, -turn)
    chooseend = turn * nums[e] + winner(nums, s, e-1, -turn)
    return turn * max(turn*choosefront, turn*chooseend)

""""""


def PredictTheWinner(nums: [int]) -> bool:
    if len(nums) % 2 == 0:
        return True
    dp = [[0 for j in range(len(nums))] for i in range(len(nums))]
    for i in range(len(nums)):
        dp[i][i] = nums[i]
    # j is the range between start and end
    # 01-> 12->23->34->02 ->13 24->13 14->04
    for j in range(1, len(nums)):
        for i in range(len(nums) - j):
            print(i, i+j)
            # 01 --> ige - 11 and i+jge - 00
            dp[i][i + j] = max(nums[i] - dp[i + 1][i + j], nums[i + j] - dp[i][i + j - 1])
    for i in dp:
        print(i)
    if dp[0][-1] >= 0:
        return True

    return False
print(PredictTheWinner([1,5,2,4,6]))
"""
[1, 4, -2, 6, 0]
[0, 5, 3, 3, 3]
[0, 0, 2, 2, 4]
[0, 0, 0, 4, 2]
[0, 0, 0, 0, 6]
True
"""

"""
01234
15246

dp[s][e] - start at s, end at e what's the max point at this time
    = Max (nums[s] - dp[s+1][e]  , nums[e] - dp[s][e-1] )
            choose start            choose end
range start from last position [n-2, n-1] <-- [0, n-1]
expand start and end until met 0-n-1 
simulate the process -- bottom-up / topdown
  01234
0 
1
2
3
4
"""


def PredictTheWinner(nums: [int]) -> bool:
    if len(nums) % 2 == 0:
        return True
        # dp=[[0 for j in range(len(nums))] for i in range(len(nums))]
    dp = [[0] * len(nums) for _ in range(len(nums))]

    # for i in range(len(nums)):
    #     dp[i][i]=nums[i]
    for s in range(len(nums) - 2, -1, -1):
        for e in range(s + 1, len(nums)):
            dp[s][e] = max(nums[s] - dp[s + 1][e], nums[e] - dp[s][e - 1])
    for i in dp:
        print(i)
    return dp[0][-1] >= 0

