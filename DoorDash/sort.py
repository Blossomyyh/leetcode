'''
\\ insertion
2312
'''
n = [5,2,3,1]
def insertion(nums):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(nums)):
        k = nums[i]
        j = i-1
        while j>=0 and nums[j]>k:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = k
        print(nums)
    return nums
print(insertion(n))

"""
\\ mergesort --> divide by 2 recursive 
& get left and right use func-merge to sort again
nlogn
"""
def mergesort(array):

    def merge(left, right):

    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
        if len(right)==0:
            return left
        if len(left)==0:
            return right
        res= []
        l = r =0
        while len(res)<len(left)+len(right):
            if left[l]<=right[r]:
                res.append(left[l])
                l +=1
            else:
                res.append(right[r])
                r+=1
            if l == len(left):
                res += right[r:]
                break
            if r== len(right):
                res += left[l:]
                break
        return res


    if len(array)<2:
        return array
    m = len(array)//2
    left = mergesort(array[:m])
    right = mergesort(array[m:])

    return merge(left, right)

"""
\\ quick sort
partition get
    i, j = l-1, l
    loop j++ 
        if j<p --> i++ exchange i,j
    (i present end of small, j present end of bigger)
    last --> place p to l+1
    return l+1
    
keep 2 part partition again
"""
def quicksort(array):
    def partition(l,r):
        p = r
        i = l-1
        for j in range(l, r):
            if array[j]<=array[p]:
                i+=1
                array[i], array[j] =  array[j],  array[i]

"""
\\ counting sort

"""
def countsort(nums):
    # The output character array that will have sorted arr
    out = [0 for i in range(len(nums))]

    count = [0 for i in range(200)]
    for i in nums:
        count[i] +=1
    print("count")
    print(count)
    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    """count idx is actual word"""
    for i in range(200):
        count[i] += count[i-1]
    print(count)
    for i in range(len(nums)):
        out[count[nums[i]] - 1] = nums[i]
        count[nums[i]] -=1
    return out
print(countsort([2,3,1,2,3]))

"""
\\ bucket sort
1) Create n empty buckets (Or lists).
    change to decimal
    0.1--0.12, 0.17
    0.23-0.22, 0.25
2) Do following for every array element arr[i].
.......a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
 O(n) time
"""
def bucketsort(x):
    arr = []
    slot = 10
    for i in range(slot):
        arr.append([])
    for j in x:
        idx = int(slot * j)
        arr[idx].append(j)
    # sort one bucket by insertionsort
    for i in range(slot):
        arr[i] = insertion(arr[i])
    # concatenate res
    k = 0
    for i in range(slot):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k+=1
    return x
