def largestRange(array):
    # Write your code here.
    array.sort()
    s, res = 0, 0
    for i in range(1, len(array)):
        if array[i] == array[i-1]+1:
            continue
        else:
            res = max(res, i-s)
            s = i

    res = max(res, len(array)-s)
    return res


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))


"""
another way to do:
use dict to record each visited num
search around for 3:
    1. search 2,1,0..
    2. search 4,5,..
"""