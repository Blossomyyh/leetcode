"""
395. Longest Substring with At Least K Repeating Characters

Input:
s = "aaabb", k = 3

Output:
3
The longest substring is "aaa", as 'a' is repeated 3 times.
Input:
s = "ababbc", k = 2

Output:
5
"""

"""
\\ recursive solution
count all with dic
start,res =0,0
single path all ele
    if ele fre<k:
        check s[start:i] max and update res
        update start by i+1
return len(s)if startnot change else get max(s[start:])
"""
from collections import Counter
def longestSubstring(s: str, k: int) -> int:
    count = Counter(s)
    start = 0
    maxres = 0
    for i, c in enumerate(s):
        if count[c] < k:
            maxres = max(maxres, longestSubstring(s[start:i], k))
            start = i + 1
    return len(s) if start == 0 else max(maxres, longestSubstring(s[start:], k))




"""
\\ divide & conquer
get counter and ch<k set
while i <len:
    if i not it <kset:
        j = i
        while j<len:
            if j not in set:
                j+=1
            else break
        add these interval
        i = j
    else
        i +=1
for each interval , do this func again(make sure every ch in set is >=k)
return max

abbaacssdff ,k2
1. abbaa, ss, ff
2. count seperately
"""
def longestRepeatedwithSlidingWindow(s, k):
    if len(s)<k:return 0
    count = Counter(s)
    hashset = set([ch for ch in count if count[ch]<k])

    # base case
    if not hashset: return len(s)

    i  =0
    inter = []
    while i<len(s):
        if s[i] in hashset:
            i+=1
        elif s[i] not in hashset:
            j = i
            while j<len(s) and s[j] not in hashset:
                j+=1
            # interval here should be s[i:j] --> jshould +1
            inter.append([i,j])
            i = j
    res = 0
    for a,b in inter:
        res = max(res, longestSubstring(s[a:b], k))
    return res
print(longestSubstring("aaabb", k=3))