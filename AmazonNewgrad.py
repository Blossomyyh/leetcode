import copy
from math import sqrt


class Solution(object):
    # Two Pointers Method:
    # Each pointer points to the next in line for entry and exit, modify arrTime array in place to get the corrected pass through time.
    # Time: O(n), space: O(1)
    def turnstile(self, numCustomers, arrTime, direction):
        start = arrTime[0]
        exiting = []
        entering = []

        for i in range(0, numCustomers):
            if direction[i] == 0:
                entering.append((arrTime[i], i))
            else:
                exiting.append((arrTime[i], i))

        res = [-1 for _ in range(numCustomers)]

        enterI = 0
        exitI = 0
        exitPrio = True
        currTime = start
        prevTime = -1

        while enterI < len(entering) and exitI < len(exiting):
            currExitTime = max(exiting[exitI][0], currTime)
            currEnterTime = max(entering[enterI][0], currTime)
            if currEnterTime < currExitTime:
                res[entering[enterI][1]] = currEnterTime
                prevTime = currEnterTime
                currTime = prevTime + 1
                enterI += 1
                exitPrio = False
            elif currExitTime < currEnterTime:
                res[exiting[exitI][1]] = currExitTime
                prevTime = currExitTime
                currTime = prevTime + 1
                exitI += 1
                exitPrio = True
            else:
                if currTime - prevTime > 1:
                    exitPrio = True
                if not exitPrio:
                    res[entering[enterI][1]] = currEnterTime
                    prevTime = currEnterTime
                    currTime = prevTime + 1
                    enterI += 1
                else:
                    res[exiting[exitI][1]] = currExitTime
                    prevTime = currExitTime
                    currTime = prevTime + 1
                    exitI += 1
                    exitPrio = True

        while enterI < len(entering):
            res[entering[enterI][1]] = max(entering[enterI][0], currTime)
            currTime += 1
            enterI += 1

        while exitI < len(exiting):
            res[exiting[exitI][1]] = max(exiting[exitI][0], currTime)
            currTime += 1
            exitI += 1
        return res


print(Solution().turnstile(4, [0, 0, 1, 5], [0, 1, 1, 0]))


def isCustomerWinner(codeList, shoppingCart):
    if not codeList: return 1
    if not shoppingCart: return 0
    i, j = 0, 0
    while i < len(codeList) and j + len(codeList[i]) <= len(shoppingCart):
        match = True
        for k in range(len(codeList[i])):
            if codeList[i][k] != 'anything' and codeList[i][k] != shoppingCart[j + k]:
                match = False
                break
        if match:
            j += len(codeList[i])
            i += 1
        else:
            j += 1
    return i == len(codeList)


# space: O(1), RTC: O(M*N), where M is number of total words in codes and N is number of number of items in the cart

print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']],
                       ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']],
                       ['banana', 'orange', 'banana', 'apple', 'apple']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']],
                       ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']))
print(isCustomerWinner([['apple', 'banana', 'apple', 'banana', 'coconut']],
                       ['apple', 'banana', 'apple', 'banana', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'orange'], ['orange', 'banana', 'orange']],
                       ['apple', 'orange', 'banana', 'orange', 'orange', 'banana', 'orange', 'grape']))
print(isCustomerWinner([['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'anything', 'banana']],
                       ['apple', 'apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([['apple', 'apple'], ['apple', 'banana']], ['apple', 'apple', 'apple', 'banana']))
print(isCustomerWinner([["anything", "apple"], ["banana", "anything", "banana"]],
                       ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]))
print(isCustomerWinner([['anything']], ['apple', 'apple', 'apple', 'banana']))

import collections
def func(l):
    visited = []
    d = collections.defaultdict(list)

    def dfs(item, output):
        if item not in visited:
            visited.append(item)
            output.append(item)
            for neighbor in d[item]:
                dfs(neighbor, output)

    if len(l) < 2:
        return l

    for item in l:
        if len(item) == 1:
            d[item[0]] = []
        else:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])

    res = []
    for item in d:
        if item not in visited:
            output = []
            dfs(item, output)
            output.sort()
            if len(res) == 0 or len(output) > len(res):
                res = output
            elif len(output) == len(res):
                res = min(res, output)

    return res
# print(func([['A', 'B'], ['D', 'E'], ['C', 'D']]) == ['C', 'D', 'E'])
# print(func([['A', 'B'], ['C', 'D'], ['F', 'E']]) == ['A', 'B'])
# print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == ['C', 'D', 'E', 'F'])
# print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == ['A', 'B', 'C', 'D', 'E', 'F'])
# print(func([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'],
#             ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
#             ['A', 'C'],]) == ['A', 'B', 'C', 'D', 'E', 'F'])
# print(func([['item1','item2'],['item3','item4'],['item4','item5']]) == ['item3', 'item4', 'item5'])
# print(func([['item1','item2'],['item2','item5'],['item3']]) == ['item1', 'item2', 'item5'])
# print(func([['item1','item2'],['item2','item3'],['item4','item5'],['item5','item6']]) == ['item1', 'item2', 'item3'])
# print(func([["item1","item2"], ["item1","item3"], ["item2","item7"], ["item3","item7"], ["item5","item6"], ["item3","item7"]]) == ['item1', 'item2', 'item3', 'item7'])



"""string -》 number from 1 to 10^6"""


def checkPrime(number):
    num = int(number)
    for i in range(2, int(num ** 0.5)):
        if ((num % i) == 0):
            return False
    return True


# A recursive function to find the minimum
# number of segments the given string can
# be divided such that every segment is a prime
def splitIntoPrimes(number):
    # If the number is null
    if (number == ''):
        return 0

    # checkPrime function is called to check if
    # the number is a prime or not.
    if (len(number) <= 6 and checkPrime(number)):
        return 1
    else:
        numLen = len(number)

        # A very large number denoting maximum
        ans = 1000000

        # Consider a minimum of 6 and length
        # since the primes are less than 10 ^ 6
        for i in range(1, (min(6, numLen) + 1)):
            if (checkPrime(number[:i])):

                # Recursively call the function
                # to check for the remaining string
                val = splitIntoPrimes(number[i:])
                if (val != -1):
                    # Evaluating minimum splits
                    # into Primes for the suffix
                    ans = min(ans, 1 + val)

                    # Checks if no combination found
        if (ans == 1000000):
            return -1
        return ans

        # Driver code


print(splitIntoPrimes("13499315"))
print(splitIntoPrimes("43"))



"""
DP 
splitDP[i] denotes the minimum number of splits required in the prefix string of length ‘i’ 
to break it into the prime subdivision.

splitDP[i + j] = min(splitDP[i + j], 1 + splitDP[i]);
"""


# A function to find the minimum
# number of segments the given string
# can be divided such that every
# segment is a prime
def checkPrime(number):
    if(len(number) == 0):
        return True
    num = int(number)
    for i in range(2,int(sqrt(num)) + 1, 1):
        if ((num % i) == 0):
            return False
    return True
def splitIntoPrimes(number):
    numLen = len(number)

    # Declare a splitdp[] array
    # and initialize to -1
    splitDP = [-1 for i in range(numLen + 1)]

    # Build the DP table in
    # a bottom-up manner
    for i in range(1, numLen + 1, 1):

        # Initially Check if the entire prefix is Prime
        if (i <= 6 and checkPrime(number[0:i])):
            splitDP[i] = 1

        # If the Given Prefix can be split into Primes
        # then for the remaining string from i to j
        # Check if Prime. If yes calculate
        # the minimum split till j
        if (splitDP[i] != -1):
            j = 1
            while (j <= 6 and i + j <= numLen):

                # To check if the substring from i to j
                # is a prime number or not
                if (checkPrime(number[i:i + j])):

                    # If it is a prime, then update the dp array
                    if (splitDP[i + j] == -1):
                        splitDP[i + j] = 1 + splitDP[i]
                    else:
                        splitDP[i + j] = min(splitDP[i + j], 1 + splitDP[i])
                j += 1

    # Return the minimum number of splits
    # for the entire string
    return splitDP[numLen]



"""
movie night

Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
Output: [0, 6]
Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215
 is the maximum number within 220 (250min - 30min)
"""
def flightDetails(arr,k):
    k -= 30
    arr = sorted(arr)
    left = 0
    right  = len(arr) -1
    max_val = 0
    while left<right:
        if arr[left]+arr[right]<=k:
            if max_val< arr[left]+arr[right]:
                max_val = arr[left] + arr[right]
                i = left
                j = right
            left += 1
        else:
            right -= 1
    return (arr[i], arr[j])


import heapq


def maxUnits(num, boxes, unitSize, unitsPerBox, truckSize):
    heap = []

    for i in range(len(boxes)):
        units_per_box = unitsPerBox[i]
        heapq.heappush(heap, (-units_per_box, boxes[i]))

    ret = 0

    while truckSize > 0 and heap:
        curr_max = heapq.heappop(heap)
        max_boxes = min(truckSize, curr_max[1])
        truckSize -= max_boxes
        ret += max_boxes * (curr_max[0] * -1)

    return ret


# test cases
print(maxUnits(3, [1, 2, 3], 3, [3, 2, 1], 3))
print(maxUnits(3, [2, 5, 3], 3, [3, 2, 1], 50))


def subsetsWithDup(self, nums):
    res = [[]]
    nums.sort()
    for i in range(len(nums)):
        k = size if i - 1 >= 0 and nums[i] == nums[i - 1] else 0
        size = len(res)
        for j in range(k, size):
            subset = copy.copy(res[j])
            subset.append(nums[i])
            res.append(subset)
    return res


# Recursive:


def subsetsWithDup(self, nums):
    res = []
    nums.sort()
    self.generateSubsets(nums, res, [], 0)
    return res


def generateSubsets(self, nums, res, curr, index):
    res.append(list(curr))
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        curr.append(nums[i])
        self.generateSubsets(nums, res, curr, i + 1)
        curr.pop()
