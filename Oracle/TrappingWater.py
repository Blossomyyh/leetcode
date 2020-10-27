"""
42. trapping water

"""
'''
Initialize ans=0ans=0
Iterate the array from left to right:

Initialize left_max=0 andright_max=0

Iterate from the current element to the beginning of array updating:
\\ left_max=max(left_max,height[j])
Iterate from the current element to the end of array updating:
\\ right_max=max(right_max,height[j])
Add  \\ min(left_max,right_max)−height[i] 
to ans

'''
def trap(height):
    left = [0]*len(height)
    right = [0]*len(height)

    for i,x in enumerate(height):
        if i==0:
            left[i] = height[i]
        else:
            left[i] = max(left[i-1], height[i])
    print(left)
    for i in range(len(height)-1, -1, -1):
        if i == len(height)-1:
            right[i] = height[i]
        else:
            right[i] = max(right[i+1], height[i])
    print(right)

    res = 0
    for i in range(len(height)):
        res += min(left[i], right[i])-height[i]
    return res
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
'''
[0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
6
'''