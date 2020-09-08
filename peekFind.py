############
# given a list find out a peek --> has both increasing and decreasing side
# brute fore
def peek(input):
    length = 0

    for i in range(1, len(input)):
        left = i-1
        right = i+1
        leftcheck = True
        rightcheck = False
        lengthCur = 1
        while left>=0 and input[left]<input[i]:
            lengthCur += 1
            left -= 1
            leftcheck = True
        while right<len(input) and input[right]<input[i]:
            lengthCur += 1
            right += 1
            rightcheck = True
        if leftcheck and rightcheck:
            length = max(length, lengthCur)
    return length


# dynamic programming!!!
# O(3n)
def peekQuicker(nums):
    l = [0]*len(nums)
    r = [0]*len(nums)
    cur = 0
    for i in range(len(nums)):
        if i ==0 or nums[i] <= nums[i-1]:
            cur = 1
        else:
            cur += 1
        l[i] = cur
    cur = 0
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums)-1 or nums[i]<=nums[i+1]:
            cur = 1
        else:
            cur += 1
        r[i] = cur
    # reverse right list --> we traversal from right to left
    # r.reverse()
    print(l, r)
    length = 0
    for i in range(len(nums)):
        length = max(length, l[i] + r[i] - 1)
    return length

print(peekQuicker([1,2,3,4,5,2,1]))

