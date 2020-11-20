"""
1423. Maximum Points You Can Obtain from Cards

Max of K cards can take either from front or end
== min of n-k cards in the middle

Solution:
    use sliding window(n-k) -> find min window in the card list
"""
def maxScore(self, cardPoints: [int], k: int) -> int:
    # edge - k>=cards / k<=0 /k==1
    if k <= 0 or not cardPoints:
        return 0
    if k >= len(cardPoints):
        return sum(cardPoints)
    if k == 1:
        return max(cardPoints[0], cardPoints[-1])

    window = len(cardPoints) - k

    # sliding window
    """\\ get sum of window \\ get res by min \\ get sumall on the go"""
    sumup = sum(cardPoints[:window])
    res = sumup
    sumall = sumup
    for i in range(window, len(cardPoints)):
        sumup = sumup - cardPoints[i - window] + cardPoints[i]
        sumall += cardPoints[i]
        res = min(res, sumup)
        # print(sumup, res)

    return sumall - res


"""
naive recursive solution
"""
def maxScore(self, cardPoints: [int], k: int) -> int:
    if k == len(cardPoints):
        return sum(cardPoints)

    def dfs(i, j, k, res=0):
        if k == 0:
            return 0
        return max(cardPoints[i] + dfs(i + 1, j, k - 1), cardPoints[j] + dfs(i, j - 1, k - 1))

    return dfs(0, len(cardPoints) - 1, k)