"""
496. Next Greater Element I

traversal from start to end
while i>stack.peek, pop out
else push
finally check the rest for -1
"""
def nextGreaterElement(nums1, nums2):
    dic = {}
    for n in nums1:
        dic[n] = -1
    stack = []
    for i in range(len(nums2)):
        if not stack or stack[-1]<nums2[i]:
            stack.append(nums2[i])
        elif stack[-1]>nums2[i]:
            big = stack.pop()
            if nums2[i] in dic:
                dic[nums2[i]] = big

    return list(dic.values())

print(nextGreaterElement([4,1,2],[1,3,4,2]))