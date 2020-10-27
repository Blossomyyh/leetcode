"""
k size deque for window
deque to implement heap (push max to 0, append following lesser one,
pop out queue when a new max come)
for  each window
    get max ele from compare deque
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if k == 1:
            return nums
        if len(nums) < 3 and k >= 2:
            return [max(nums)]
        # append idx from max to min

        maxheap = deque()
        res = []

        # store index
        def clearmax():
            while maxheap:
                if nums[i] > nums[maxheap[-1]]:
                    maxheap.pop()
                else:
                    break
            maxheap.append(i)

        # initialize queue
        for i in range(k):
            clearmax()
        res.append(nums[maxheap[0]])

        # get max on the fly
        for i in range(k, len(nums)):
            clearmax()
            if maxheap[0] < i - k + 1:
                maxheap.popleft()
            res.append(nums[maxheap[0]])

        return res


print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))


"""
\\ DP problem

left - store max for each block from left to right
right - store max from right to left
get max from left[endblock] & right[startblock]
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        left = [0]*len(nums)
        right = [0]*len(nums)
        # left : store max ele from 0 to i
        left[0] = nums[0]
        for i in range(1, len(nums)):
            if i%k==0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(nums[i], left[i-1])
        # right : store max ele from i to 0
        right[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, -1, -1):
            if i%k==0:
                # block start
                right[i] = nums[i]
            else:
                right[i] = max(nums[i], right[i+1])
        res = []
        for i in range(len(nums)-k+1):
            res.append(max(right[i], left[i+k-1]))
        return res


from collections import deque
def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # Checking for base case
    if not nums:
        return []
    if k == 0:
        return nums
    # Defining Deque and result list
    deq = deque()
    result = []

    # First traversing through K in the nums and only adding maximum value's index to the deque.
    # Note: We are olny storing the index and not the value.
    # Now, Comparing the new value in the nums with the last index value from deque,
    # and if new valus is less, we don't need it

    for i in range(k):
        while len(deq) != 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break

        deq.append(i)

    # Here we will have deque with index of maximum element for the first subsequence of length k.

    # Now we will traverse from k to the end of array and do 4 things
    # 1. Appending left most indexed value to the result
    # 2. Checking if left most is still in the range of k (so it only allows valid sub sequence)
    # 3. Checking if right most indexed element in deque is less than the new element found, if yes we will remove it
    # 4. Append i at the end of the deque  (Not: 3rd and 4th steps are similar to previous for loop)

    for i in range(k, len(nums)):
        result.append(nums[deq[0]])

        if deq[0] < i - k + 1:
            deq.popleft()

        while len(deq) != 0:
            if nums[i] > nums[deq[-1]]:
                deq.pop()
            else:
                break

        deq.append(i)

    # Adding the maximum for last subsequence
    result.append(nums[deq[0]])

    return result
maxSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3)