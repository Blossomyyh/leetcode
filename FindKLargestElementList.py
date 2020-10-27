"""
Find the Kth Largest Element in a List

1. heap - klogn time to find largest element

 // heap is a data structure and which is partially sorted where each value is greater than child value.
 // pop one out and you can get rid of this and you would just do this again.
 // each sifting operation takes logarithmic time
 //obtain the k largest element Now implementing a completely you can do this using like a priority queue
 //  I would think that's a pretty optimal solution.

2. !!quick select


"""
import heapq
import random
class Solution(object):

    def findKLargestSort(self, nums, k):
        return sorted(nums)[len(nums)-k]

    """
        \\ heap cannot use key
            only smarllest heap - each key from small to big
            X heapify
            X heappop

        \\ only nlargest/nsmallest
                has key argument \\ lambda x:() \\ no reverse -- has to make(-int), X(-str) -> (ord(ch)..)

        \\ sort has key and reverse=True/False
                can sort by x[1] alphabetically
                then sort by x[0]!

    """
    def findKLargest2(self, nums, k):
        """largest/smallest"""
        res = heapq.nlargest(k, nums, key=lambda x: (x[0],x[1]))
        print(res)
        # [(2, 'cs'), (1, 'ds'), (1, 'abs'), (1, 'a')]
        minimum = heapq.nsmallest(k, nums)
        print(minimum)
        # [(1, 'a'), (1, 'abs'), (1, 'ds'), (2, 'cs')]

        """heap sort"""
        heapq.heapify(nums)
        while k >0:
            print(heapq.heappop(nums))
            k -= 1
        # (1, 'a')
        # (1, 'abs')
        # (1, 'ds')
        # (2, 'cs')

        """sort 2 times"""
        l = [(3, 'one'), (2, 'was'), (2, 'two'), (1, 'too'), (1, 'racehorse'), (1, 'a')]
        l.sort(key=lambda x: x[1])
        # [(1, 'a'), (3, 'one'), (1, 'racehorse'), (1, 'too'), (2, 'two'), (2, 'was')]
        print(l)
        l.sort(key=lambda x: x[0], reverse=True)
        # l.sort(reverse=True)
        print(l)
        # [(3, 'one'), (2, 'two'), (2, 'was'), (1, 'a'), (1, 'racehorse'), (1, 'too')]
        return res[-1]


print(Solution().findKLargest2([(1, 'abs'), (1,'a'), (1, 'ds'), (2, 'cs')], 4))

"""
quicksort

in linear time
so the way looks like is 
 you pick a pivot and 
 ideally it is the center value 
 you rearrange the array such that every element 
 that's less than that pivot value is on the left side 
 and everything that is greater is on the right side. 

    So it is partially sorted. 
    So for instance, we choose the pivot,
     maybe we pick four. 
     And we start by just putting it to the beginning of the array.
     And now we're going to rearrange the elements here. 
     And at the end, we're going to bring that value back to where it should belong. 
     
     Once we find out the index. So we take a look at the value here
      the array looks like four. Or five to three six eight.
      So we've just simply swapped 4 and 3 here.
      
      two is less than the pivot value for it, right?
       So we're going to swap two with the first open position. 
       So, We move to here five here and then we increment this by one 
       so this is the next index of the open position that we can put the next value 
       so that's all looking good 
    
    we would have partitioned around four so that's at the end of the first iteration 
    we will continue doing this quick select again on only one half of the array 
    so we do it for this set five six and eight at this time we'll partition around the value six. 


"""

