"""

for k from i to j
    res(i, j) = min(res(i, k) + res(k + 1, j) + max(arr[i] ... arr[k]) * max(arr[k + 1] ... arr[j]))

Greedy approach ---> O(n ^ 2)
"""


def mctFromLeafValues(self, arr) -> int:
    res = 0
    while len(arr) > 1:
        index = arr.index(min(arr))
        if 0 < index < len(arr) - 1:
            res += arr[index] * min(arr[index - 1], arr[index + 1])
        else:
            res += arr[index] * (arr[index + 1] if index == 0 else arr[index - 1])
        arr.pop(index)
    return res

'''
3. Monotonic stack approach ---> O(n)
In the greedy approach of 2), 
every time we delete the current minimum value, 
we need to start over and find the next smallest value again, 
so repeated operations are more or less involved. 
To further accelerate it, one observation is that for each leaf node in the array, 
when it becomes the minimum value in the remaining array, 
its left and right neighbors will be the first bigger value in the original array to its left and right. 
This observation is a clue of a possible monotonic stack solution as follows.
'''
class Solution:
    def mctFromLeafValues(self, arr) -> int:
        stack = [float('inf')]
        res = 0
        for num in arr:
            while stack and stack[-1] <= num:
                cur = stack.pop()
                if stack:
                    res += cur * min(stack[-1], num)
            stack.append(num)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res
