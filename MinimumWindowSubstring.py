"""
76. Minimum Window Substring
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
"""
from collections import Counter
def minWindow(search_string, target):
    if not search_string and not target:
        return ""
    dic = Counter(target)
    required = len(dic)

    # The filtering criteria is that the character should be present in t.
    filteredS = []
    for i, char in enumerate(search_string):
        if char in dic:
            filteredS.append((i, char))

    left, right = 0, 0
    formed = 0
    windowCount = {}

    ans = float('inf'), None, None

    while right<len(filteredS):
        ch = filteredS[right][1]
        windowCount[ch] = windowCount.get(ch, 0) + 1
        if windowCount[ch] == dic[ch]:
            formed +=1

        while  left <= right and formed==required:
            chl = filteredS[left][1]

            # save small window
            end = filteredS[right][0]
            start = filteredS[left][0]

            # update ans
            if end - start+1<ans[0]:
                ans = (end -  start+1, end, start)
            windowCount[chl] -= 1
            if windowCount[chl] <dic[ch]:
                formed -= 1
            left +=1
        right+=1

    return "" if ans[0] == float('inf') else search_string[ans[1]: ans[2]+1]

s = "ADOBECODEBANC"
t  = "ABC"
print(minWindow(s, t))