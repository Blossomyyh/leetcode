class Solution:
    # Mathematical: Digital Root
    #     Could you do it without any loop/recursion in O(1) runtime?
    def addDigits(self, num: int) -> int:
        n = num
        while n >= 10:
            sum = 0
            while n > 0:
                sum += n % 10
                #                 use mode 10 to get the digit
                # then we shift the number one decimal place using n equals n divided by 10
                # and we just add those up, and we have another out loop here
                # log10of k in terms of runtime
                n = n // 10
            n = sum
        return sum

    def digitalroot(self, num):
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9



import heapq
from collections import Counter
from collections import defaultdict
def removeProduct(num, ids, rem):
    # WRITE YOUR CODE HERE
    ids.sort()
    while rem:
        ids.pop()
        rem -= 1
    count = Counter(ids)
    print(len(count))
    return len(count)
removeProduct(4,[1,1,5,5],2)