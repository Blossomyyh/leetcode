"""
3. Longest Substring Without Repeating Characters

use set to store
if new add to set and update length j++
not then:
    delete a[i] in set i++
"""




class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        visited = set()
        i, j = 0, 0
        res = 0
        while i <= j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                res = max(res, j - i)
            else:
                visited.remove(s[i])
                i += 1
        return res

"""
optimized:
\\ hashmap to store last visited index
0-end 
start =0 
if redundancy and start<last visited[i]
    start = last visited[i] + 1
else:
    res update
update dic in each iteration


"""


def lengthOfLongestSubstring(self, s: str) -> int:
    # define a mapping of the characters to its index.
    dic = {}
    i, res = 0, 0
    for j in range(len(s)):
        if s[j] in dic and i <= dic[s[j]]:
            i = dic[s[j]] + 1
        else:
            res = max(res, j - i + 1)
        dic[s[j]] = j
    return res
