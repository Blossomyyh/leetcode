"""
704. Binary Search


"""
def search(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    s, e = 0, len(nums) - 1
    while s <= e:
        mid = s + (e - s) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            s = mid + 1
        elif nums[mid] > target:
            e = mid - 1
    return -1

'''
Python
implementation
of

\\  1.
bisect_left(arr, var, lo, hi)

if lo < 0:
    raise ValueError('lo must be non-negative')
if hi is None:
    hi = len(a)

while lo < hi:
    mid = (lo + hi) // 2

    if a[mid] < x:
        lo = mid + 1
    else:
        hi = mid
return lo




\\ 2.
bisect_right(arr, var, lo, hi)

if lo < 0:
    raise ValueError('lo must be non-negative')
if hi is None:
    hi = len(a)

while lo < hi:
    mid = (lo + hi) // 2

    if x < a[mid]:
        hi = mid
    else:
        lo = mid + 1
#return lo

'''