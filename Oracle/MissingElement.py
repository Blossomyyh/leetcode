"""
1060. Missing Element in Sorted Array

binary search
logn
"""
def missingElement(self, nums, k: int) -> int:
    if not nums or k==0:
        return 0
    #length
    diff = nums[-1]-nums[0]+1
    # how many missing here
    missing = diff -len(nums)

    # if k is larger than the number of mssing
    if k>missing:
        return nums[-1]+k-missing

    """binary search"""
    left, right = 0, len(nums)-1
    while left+1<right:
        mid = (left+right)//2
        missing = nums[mid]-nums[left] - (mid-left)
        if missing<k:
            # KEY: move left forward,
            # minus the missing words of this range
            left = mid
            k -= missing
        else:
            right = mid

    return nums[left]+k